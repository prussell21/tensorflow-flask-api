import tensorflow as tf
import json
import numpy as np
from flask import Flask, request

app = Flask(__name__)


@app.route('/api/', methods=['POST'])
def predict():
    data = request.json
    params = data['params']
    arr = np.array(data['arr'])
    
    formatted_img = arr.reshape(-1, 28 * 28) / 255.0
    prediction = new_model.predict(formatted_img).argmax()
    
    return str(prediction)


if __name__ == '__main__':
    new_model = tf.keras.models.load_model('mnist_model.h5')
    app.run(debug=True, host='0.0.0.0')
