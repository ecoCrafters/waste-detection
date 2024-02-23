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

# How to use it?


## Local Development

### Build and Run Docker

Build the docker file by using command below in the terminal.

```shell
docker build -t <image_name> .
```

The command above only executes once.
Except if you change or create a new dockerfile, you need to rebuild the docker image.
Run docker image that already built in the previous step.

```shell
docker run -p 8501:8501 <image_name>
```

## Stop Docker

To stop docker services, type the following command in your terminal.

```shell
docker stop <container_id>
```

## Deploy to Cloud Run

To deploy the model to Cloud Run, you build the docker image and push it to the Google Container Registry.
Then, you can deploy the model to Cloud Run.
You can do so by running the following command in your terminal.
Substitute `<project_id>` with your project id on GCP and `<image_name>` with the name of the image you want to use.

```shell
docker build -t gcr.io/<project_id>/<image_name> .
```

Push the image to the Google Container Registry.

```shell
docker push gcr.io/<project_id>/<image_name>
```

Deploy the model to Cloud Run.
You can either use the Google Cloud Console, select the image you've pushed,
and set the container port to 8501, or run the following command in your terminal.
Substitute `<project_id>` with your project id on GCP, `<image_name>`
with the name of the image you want to use, and `<service_name>` with the name of the service you want to use.

```shell
gcloud run deploy <service_name> \
--image=gcr.io/<project_id>/<image_name> \
--allow-unauthenticated \
--port=8501 \
--cpu-boost \
--region=<region>\
--project=<project_id>
```

## Prediction Testing

Create a file named .env and fill it with the following content:

```shell
ENDPOINT=<your_cloud_run_endpoint>
MODEL_NAME=<your_model_name>
```

Change the `<your_cloud_run_endpoint>` with the endpoint of your Cloud Run service.
Make sure you set the MODEL_NAME value the same as the model name stated in the Dockerfile.
If you are intended to use local development,
you can either set the ENDPOINT value to `http://localhost:8501` or leave it empty.

In this repository, there is a `sample_image/000001.jpg` image that can be used for prediction testing.
To run the prediction test, make sure you have the required packages installed.
You can do so by running the following command in your terminal.

```shell
pip install -r requirements.txt
```

Then you can run `req.py`, which contains code for making a request to the server and show you the prediction result.
To run the code, type the following command in your terminal.

```shell
python req.py
```
