import numpy as np

from joblib import load
from flask import Flask, jsonify, request

app =  Flask(__name__)

id2label = {0: 'excitment',
 1: 'GetWeather',
 2: 'Cancellation',
 3: 'Affirmation',
 4: 'BookRestaurant',
 5: 'PlayMusic',
 6: 'SearchScreeningEvent',
 7: 'SearchCreativeWork',
 8: 'Book Meeting',
 9: 'AddToPlaylist',
 10: 'RateBook',
 11: 'Greetings'}

@app.route('/predict', methods=['POST'])
def predict():
    text = request.get_json()
    print(text)

    preds = intent_clf.predict_proba(text)
    proba = np.max(preds)
    intent = id2label[np.argmax(preds)]

    return jsonify({'intent': intent, 'confidence': proba})

if __name__ == "__main__":
    intent_clf = load('intent_clf.joblib')

    app.run(debug=True)