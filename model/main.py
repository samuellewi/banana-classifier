import os
import matplotlib.pyplot as plt
import tensorflow as tf
from tensorflow.keras import layers, models
from tensorflow.keras.applications import MobileNetV2
import kagglehub

# Enable mixed precision for faster training on Apple Silicon
tf.keras.mixed_precision.set_global_policy('mixed_float16')

# --- 1. CONFIGURATION ---
# Download latest version
path = kagglehub.dataset_download("shahriar26s/banana-ripeness-classification-dataset")

print("Path to dataset files:", path)
BASE_DIR = os.path.join(path, "Banana Ripeness Classification Dataset")
BATCH_SIZE = 32  # Good balance for MobileNetV2 training
IMG_SIZE = (224, 224)
EPOCHS = 8

# --- 2. DATA PREPARATION FUNCTION ---
def load_and_relabel_data(directory):
    dataset = tf.keras.utils.image_dataset_from_directory(
        directory,
        shuffle=True,
        batch_size=BATCH_SIZE,
        image_size=IMG_SIZE
    )
    
    class_names = dataset.class_names
    # Identify the index of the 'rotten' folder
    rotten_idx = class_names.index('rotten')
    
    def map_labels(images, labels):
        # 1.0 if folder is 'rotten', 0.0 for everything else
        is_rotten = tf.equal(labels, rotten_idx)
        new_labels = tf.cast(is_rotten, tf.float32)
        return images, new_labels

    return dataset.map(map_labels)

# Load the three distinct sets
train_ds = load_and_relabel_data(os.path.join(BASE_DIR, 'train'))
val_ds = load_and_relabel_data(os.path.join(BASE_DIR, 'valid'))
test_ds = load_and_relabel_data(os.path.join(BASE_DIR, 'test'))

# Optimize performance
AUTOTUNE = tf.data.AUTOTUNE
train_ds = train_ds.cache().shuffle(1000).prefetch(buffer_size=AUTOTUNE)
val_ds = val_ds.cache().prefetch(buffer_size=AUTOTUNE)
test_ds = test_ds.cache().prefetch(buffer_size=AUTOTUNE)

# --- 3. MODEL ARCHITECTURE ---

# Data augmentation layers
data_augmentation = models.Sequential([
    layers.RandomFlip("horizontal_and_vertical"),
    layers.RandomRotation(0.2),
])

# Load pre-trained MobileNetV2 base (frozen)
base_model = MobileNetV2(
    input_shape=(224, 224, 3),
    include_top=False,  # Remove the classification head
    weights='imagenet'  # Use pre-trained ImageNet weights
)
base_model.trainable = False  # Freeze the base model

# Build the complete model
model = models.Sequential([
    data_augmentation,
    layers.Rescaling(1./255, input_shape=(224, 224, 3)),
    base_model,
    layers.GlobalAveragePooling2D(),
    layers.Dense(128, activation='relu'),
    layers.Dropout(0.5),
    layers.Dense(1, activation='sigmoid')
])

# --- 4. COMPILATION AND TRAINING ---
model.compile(
    optimizer='adam',
    loss='binary_crossentropy',
    metrics=['accuracy']
)

history = model.fit(
    train_ds,
    validation_data=val_ds,
    epochs=EPOCHS
)

# --- 5. EVALUATION ---
test_loss, test_acc = model.evaluate(test_ds)
print(f"Final Test Accuracy: {test_acc*100:.2f}%")

# --- 6. SAVE ---
model.save('rotten_banana_mobilenet_224_model.h5')