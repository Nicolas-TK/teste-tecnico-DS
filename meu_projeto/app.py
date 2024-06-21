from flask import Flask, request, jsonify
import pickle
import numpy as np

app = Flask(__name__)

model = pickle.load(open('model.pkl', 'rb'))

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json(force=True)
    prediction = model.predict([np.array(data['input'])])
    output = {'prediction': int(prediction[0])}
    return jsonify(output)

if __name__ == '__main__':
    app.run(port=5000, debug=True)
