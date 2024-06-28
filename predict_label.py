import tensorflow as tf
import numpy as np
from PIL import Image

class_map = {0: 'Apple', 1: 'Banana', 2: 'Broccoli', 3: 'Carrots', 4: 'Cauliflower', 5: 'Chili', 6: 'Coconut', 
             7: 'Cucumber', 8: 'Custard apple', 9: 'Dates', 10: 'Dragon', 11: 'Egg', 12: 'Garlic', 13: 'Grape', 
             14: 'Green Lemon', 15: 'Jackfruit', 16: 'Kiwi', 17: 'Mango', 18: 'Okra', 19: 'Onion', 20: 'Orange', 
             21: 'Papaya', 22: 'Peanut', 23: 'Pineapple', 24: 'Pomegranate', 25: 'Star Fruit', 26: 'Strawberry', 
             27: 'Sweet Potato', 28: 'Watermelon', 29: 'White Mushroom'}


model = tf.keras.models.load_model('model_2.1.h5')

def predict_label(test_image_input):
    predicted_label = np.argmax(model.predict(test_image_input))
    predicted_class = class_map[predicted_label]
    return predicted_class


def predict_label_wrapper(test_image_path):
    img = Image.open(test_image_path)
    img = img.resize((240, 240))
    img_arr = np.array(img) / 255.0
    img_input = img_arr.reshape((1,) + img_arr.shape)
    predicted_class = predict_label(img_input)
    return predicted_class