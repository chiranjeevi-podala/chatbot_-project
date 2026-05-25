import numpy as np
import random
import json
import pickle
from tensorflow.keras.models import load_model

model = load_model("model.h5")

words = pickle.load(open("words.pkl", "rb"))
labels = pickle.load(open("labels.pkl", "rb"))

with open("data.json") as file:
    data = json.load(file)

def bag_of_words(sentence, words):
    sentence_words = sentence.lower().split()

    bag = [0] * len(words)

    for s in sentence_words:
        for i, w in enumerate(words):
            if w == s:
                bag[i] = 1

    return np.array(bag)

def get_response(msg):
    bow = bag_of_words(msg, words)
    result = model.predict(np.array([bow]))[0]

    index = np.argmax(result)
    tag = labels[index]

    for intent in data["intents"]:
        if intent["tag"] == tag:
            return random.choice(intent["responses"])