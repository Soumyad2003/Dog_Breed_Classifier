import streamlit as st
import tensorflow as tf
from PIL import Image
import numpy as np
import tf_keras
import tensorflow_hub as hub

def load_model(model_path):
  """
  Loads a saved model from a specified path.
  """
  print(f"Loading saved model from: {model_path}")
  model = tf_keras.models.load_model(model_path,
                                     custom_objects = {"KerasLayer": hub.KerasLayer})
  return model
# Load your trained model
model = load_model('20250725-133035-full-image-set-mobilenetv2-Adam.h5') # Replace with the actual path to your model file

# Load the list of unique breeds
# You'll need to save your unique_breeds list from the notebook
# For example, you can save it as a text file and load it here
with open('unique_breeds.txt', 'r') as f:
    unique_breeds = [line.strip() for line in f]

# Image processing function (from your notebook)
IMG_SIZE = 224
def process_image(image):
    """
    Takes a PIL image and preprocesses it for the model.
    """
    image = image.resize((IMG_SIZE, IMG_SIZE))
    image = np.array(image)
    image = tf.image.convert_image_dtype(image, tf.float32)
    image = tf.expand_dims(image, axis=0) # Add a batch dimension
    return image

# Streamlit app interface
st.title('🐶 Dog Breed Prediction')
st.write('Upload an image of a dog, and the model will predict its breed.')

uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    # Display the uploaded image
    image = Image.open(uploaded_file)
    st.image(image, caption='Uploaded Image.', use_container_width=True)

    # Add a spinner for user feedback
    with st.spinner("Classifying..."):
        processed_image = process_image(image)
        prediction = model.predict(processed_image)

        # Get the top prediction
        predicted_breed_index = np.argmax(prediction)
        predicted_breed = unique_breeds[predicted_breed_index]
        confidence = np.max(prediction)

    # Display the result in a clean and attractive way
    st.success(f"I'm pretty sure this is a...")

    st.metric(
        label="Predicted Breed",
        value=predicted_breed,
        delta=f"{confidence:.2%} Confidence"
    )

    # Add a little celebration
    st.balloons()