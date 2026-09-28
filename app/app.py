from flask import Flask, request, jsonify, render_template
import tensorflow as tf
import numpy as np
from PIL import Image
import io
import os

app = Flask(__name__)

# Load the model at startup
MODEL_PATH = os.path.join(os.path.dirname(__file__), '..', 'model', 'rotten_banana_mobilenet_224_model.h5')
model = None

def load_model():
    global model
    try:
        model = tf.keras.models.load_model(MODEL_PATH)
        print("Model loaded successfully!")
    except Exception as e:
        print(f"Error loading model: {e}")
        print("Please ensure the model file exists at:", MODEL_PATH)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if model is None:
        return jsonify({'error': 'Model not loaded'}), 500

    if 'image' not in request.files:
        return jsonify({'error': 'No image file provided'}), 400

    file = request.files['image']

    try:
        # Open image with PIL
        img = Image.open(io.BytesIO(file.read()))

        # Convert to RGB (handles RGBA from canvas)
        img = img.convert('RGB')

        # Resize to model input size (224x224)
        img = img.resize((224, 224))

        # Convert to numpy array
        img_array = np.array(img, dtype=np.uint8)

        # Add batch dimension: (1, 416, 416, 3)
        img_array = np.expand_dims(img_array, axis=0)

        # Model has built-in Rescaling layer, so keep values in 0-255 range
        # Run prediction
        prediction = model.predict(img_array)

        # Extract confidence score (sigmoid output)
        confidence = float(prediction[0][0])

        # Classify: > 0.5 means "Rotten", otherwise "Fresh"
        is_rotten = confidence > 0.5
        result = "Rotten" if is_rotten else "Fresh"

        return jsonify({
            'result': result,
            'confidence': confidence,
            'is_rotten': is_rotten
        })

    except Exception as e:
        print(f"Error processing image: {e}")
        return jsonify({'error': 'Failed to process image'}), 500

if __name__ == '__main__':
    load_model()
    app.run(debug=True)
