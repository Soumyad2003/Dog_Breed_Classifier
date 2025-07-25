# 🐶 DogBreedAI - Dog Breed Classifier with Streamlit

An end-to-end deep learning project that classifies dog breeds from images using a fine-tuned MobileNetV2 model. The app is deployed using **Streamlit**, supports both single and batch image uploads, and predicts among 120+ dog breeds.

## 🚀 Demo

Upload your dog image or run batch prediction on a folder:
```
streamlit run streamlit_app.py
```

## 📂 Project Structure
```
DogBreedAI/
├── streamlit_app.py          # Streamlit UI
├── dog_breed_model.h5        # Trained TensorFlow model
├── app_helpers/              # (Optional) helper functions
├── sample_images/            # For quick testing
└── README.md
```

## 🧠 Model Details
- **Architecture:** MobileNetV2 (from TensorFlow Hub)
- **Framework:** TensorFlow/Keras
- **Classes:** 120 Dog Breeds
- **Data Source:** [Kaggle Dog Breed Identification Dataset](https://www.kaggle.com/c/dog-breed-identification)
- **Training Strategy:**
  - Transfer Learning using MobileNetV2
  - Image preprocessing and augmentation
  - Trained with early stopping and validation monitoring

## 🔍 Features
- 🖼️ Classifies single dog image via Streamlit upload
- 📁 Batch classification from local folder paths
- 🧠 Displays top prediction with confidence
- 🪄 Uses transfer learning for efficient training
- ⚡ Real-time inference using optimized model

## 📦 Installation
```bash
pip install -r requirements.txt
```

## ⚙️ Usage
```bash
# Run the app
streamlit run streamlit_app.py
```

## ✅ Requirements
```
tensorflow-cpu
streamlit
numpy
pillow
```

## 🏷️ Example Prediction
```
Input: golden_retriever.jpg
Output: "Predicted Breed: golden_retriever (Confidence: 98.2%)"
```

## 📌 Skills & Concepts Practiced
- Deep Learning & Image Classification
- Transfer Learning & MobileNetV2
- Model Deployment via Streamlit
- Real-world ML Inference on Custom Inputs
