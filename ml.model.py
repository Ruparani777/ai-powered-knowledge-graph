import tensorflow as tf
import numpy as np

# Build a simple TensorFlow model for product classification
def create_model():
    model = tf.keras.models.Sequential([
        tf.keras.layers.Dense(64, activation='relu', input_shape=(2,)),  # 2 input features: category and price
        tf.keras.layers.Dense(32, activation='relu'),
        tf.keras.layers.Dense(1, activation='sigmoid')  # Binary output: valid (1) or invalid (0)
    ])
    
    model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
    return model

# Dummy training data (category encoded as 0, 1, or 2; price as normalized value)
X_train = np.array([
    [0, 0.5],  # Electronics, normalized price
    [1, 0.2],  # Home, normalized price
    [2, 0.8]   # Books, normalized price
])

y_train = np.array([1, 0, 1])  # 1 for valid, 0 for invalid

# Train the model
model = create_model()
model.fit(X_train, y_train, epochs=50, verbose=1)

# Function to make predictions
def predict_validity(product_features):
    return model.predict(np.array([product_features]))[0][0]
