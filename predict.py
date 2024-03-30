import os
import cv2
import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras import backend as K

# Define custom metric functions for prediction
def mse_metric(y_true, y_pred):
    return K.mean(K.square(y_true - y_pred))

def r_square(y_true, y_pred):
    SS_res =  K.sum(K.square(y_true - y_pred)) 
    SS_tot = K.sum(K.square(y_true - K.mean(y_true))) 
    r2 = 1 - SS_res / (SS_tot + K.epsilon())
    return K.clip(r2, 0, 1)

# Load the model with custom metrics
model_path = 'trained_model.h5'
model = load_model(model_path, custom_objects={'mse_metric': mse_metric, 'r_square': r_square})

imageToPredictFolder = "ImageToPredict"

# Preprocess image
def preprocess_image(image_path):
    img = cv2.imread(image_path)
    if img is None:
        print(f"Error: Unable to read image: {image_path}")
        return None
    img = cv2.resize(img, (128,128))
    img_array = img/255.0
    return img_array

# Predict AQI from image/images
def predict_aqi(image_path,model):
    img_array = preprocess_image(image_path)
    if img_array is None:
        return None
    img_array = np.expand_dims(img_array, axis=0)
    prediction = model.predict(img_array)
    return prediction[0][0]

predicted_aqi_list = []
for filename in os.listdir(imageToPredictFolder):
    if filename.endswith(('.png', '.jpg', '.jpeg')):
        image_path = os.path.join(imageToPredictFolder, filename)
        predicted_aqi = predict_aqi(image_path, model)
        if predicted_aqi is not None:
            print(f"Image: {filename}, Predicted AQI: {predicted_aqi}")
            predicted_aqi_list.append((filename, predicted_aqi))

# Print the list of predicted AQI for all images
print("Predicted AQI List:")
print(predicted_aqi_list)
