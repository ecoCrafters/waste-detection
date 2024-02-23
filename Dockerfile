FROM tensorflow/serving

# Specify the path the exported model for copying it to the container
COPY ./exported_models/ssd_mobnet_7_class/saved_model /models/ssd_mobnet_320_7/1

# Specify the model base path and the model name
ENV MODEL_BASE_PATH=/models
ENV MODEL_NAME=ssd_mobnet_320_7

# Expose the default gRPC port
EXPOSE 8500

# Start TensorFlow Serving
CMD tensorflow_model_server --port=8500 --rest_api_port=8501 --model_base_path=${MODEL_BASE_PATH} --model_name=${MODEL_NAME}
