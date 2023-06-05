import numpy as np
from PIL import Image
import json
import requests
import matplotlib.pyplot as plt
import matplotlib.patches as patches

def load_image_into_numpy_array(path):
    return np.array(Image.open(path))

PATH = './000001.jpg'

test_image = load_image_into_numpy_array(PATH)
reshaped_image = np.expand_dims(test_image, 0)
data = json.dumps({"signature_name": "serving_default", "instances": reshaped_image.tolist()})
headers = {"content-type": "application/json"}
json_response = requests.post('http://localhost:8501/v1/models/my_ssd_mobnet:predict', data=data, headers=headers)
predictions = json.loads(json_response.text)['predictions']

boxes = predictions[0]['detection_boxes']
scores = predictions[0]['detection_scores']
labels = predictions[0]['detection_classes']

# Visualize the results
image = test_image # Load or obtain the image corresponding to the predictions

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
    label_text = f'Class: {label}, Score: {score:.2f}'
    ax.text(left, top - 5, label_text, color='r')

# Show the image with bounding boxes and labels
plt.show()
