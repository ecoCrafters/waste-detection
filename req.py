import numpy as np
from PIL import Image
import json
import requests
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import dotenv
import os

# Load the environment variables
dotenv.load_dotenv()
ENDPOINT = os.getenv('ENDPOINT') if os.getenv('ENDPOINT') else 'http://localhost:8501'
MODEL_NAME = os.getenv('MODEL_NAME')
# specify the path to the image
PATH = 'sample_image/000001.jpg'


def read_label_map(label_map_path):
    item_id = None
    item_name = None
    items = {}

    with open(label_map_path, "r") as file:
        for line in file:
            line.replace(" ", "")
            if line == "item{":
                pass
            elif line == "}":
                pass
            elif "id" in line:
                item_id = int(line.split(":", 1)[1].strip())
            elif "name" in line:
                item_name = line.split(":", 1)[1].replace("'", "").replace('"', "").strip()

            if item_id is not None and item_name is not None:
                items[item_id] = item_name
                item_id = None
                item_name = None

    return items


def load_image_into_numpy_array(path):
    img = Image.open(path).resize((320,320))
    return np.array(img)


test_image = load_image_into_numpy_array(PATH)
reshaped_image = np.expand_dims(test_image, 0)
data = json.dumps({"signature_name": "serving_default", "instances": reshaped_image.tolist()})
headers = {"content-type": "application/json"}
json_response = requests.post(f'{ENDPOINT}/v1/models/{MODEL_NAME}:predict', data=data, headers=headers)
predictions = json.loads(json_response.text)['predictions']
label_map = read_label_map('label_map.pbtxt')

boxes = predictions[0]['detection_boxes']
scores = predictions[0]['detection_scores']
labels = predictions[0]['detection_classes']

# Visualize the results
# Load or obtain the image corresponding to the predictions
image = test_image

# Create figure and axes
fig, ax = plt.subplots(1)
ax.imshow(image)

# Iterate over the bounding boxes and plot them
for box, score, label in zip(boxes, scores, labels):
    ymin, xmin, ymax, xmax = box

    if score < 0.3:
        continue

    # Calculate the coordinates of the bounding box in pixels
    width, height = image.shape[1], image.shape[0]
    left = xmin * width
    right = xmax * width
    top = ymin * height
    bottom = ymax * height

    # Create a rectangle patch
    rect = patches.Rectangle((left, top), right - left, bottom - top, linewidth=1, edgecolor='r', facecolor='none')

    # Add the rectangle patch to the axes
    ax.add_patch(rect)

    # Add the class label and score as text
    label_text = f'Class: {label_map[int(label)]}, Score: {score:.2f}'
    ax.text(left, top - 5, label_text, color='r')

# Show the image with bounding boxes and labels
plt.show()
