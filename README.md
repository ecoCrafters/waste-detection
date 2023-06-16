# Serving Model

Sample Response:
```json
{
  "predictions": [
    {
      "detection_classes": [3.0, 1.0, 4.0, ...],
      "raw_detection_scores": [...],
      "detection_anchor_indices": [...],
      "num_detections": 100.0,
      "detection_multiclass_scores": [...],
      "raw_detection_boxes": [...],
      "detection_boxes": [
        [
          0.130028903, 
          0.342044801, 
          0.937894762, 
          0.624998093
        ],
        [
          0.130028903, 
          0.342044801, 
          0.937894762, 
          0.624998093
        ],
        [
          0.107640505, 
          0.343304783, 
          0.935199499, 
          0.636344671
        ],
        ...
      ],
      "detection_scores": [
        0.307633072, 0.294662386, 0.26344031, ...
      ]
    }
  ]
}
```

## How to use it?
# Build and Run Docker
Build the docker file by using command below in the terminal.
```
docker build -t <image_name> .
```
The command above only execute once. Except if you change or create a new dockerfile, you need to rebuild the docker image.
Run docker image that already built in the previous step.
```
docker run -p 8501:8501 <image_name>
```
# Prediction Testing
In this repository, there is a 000001.jpg image that can be used for prediction testing. To run the prediction test, you can simply run req.py, which contains code for making a request to the server. To run the code, type the following command in your terminal.
```
python req.py
```
# Stop Docker
To stop docker services, type the following command in your terminal.
```
docker stop <container_id>
```
