import numpy as np
from PIL import Image
import json
import requests

def load_image_into_numpy_array(path):
    return np.array(Image.open(path))

PATH = './IMG_1475.jpg'

test_image = load_image_into_numpy_array(PATH)
reshaped_image = np.expand_dims(test_image, 0)
data = json.dumps({"signature_name": "serving_default", "instances": reshaped_image.tolist()})
headers = {"content-type": "application/json"}
json_response = requests.post('http://localhost:8501/v1/models/ssd_mobnet_7_class:predict', data=data, headers=headers)
with open('response.json', 'w') as f:
    json.dump(json_response.json(), f, indent=4)
