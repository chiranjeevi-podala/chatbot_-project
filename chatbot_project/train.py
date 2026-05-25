import json
import numpy as np
import pickle
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
import nltk

nltk.download('punkt')

with open("data.json") as file:
    data = json.load(file)

words = []
labels = []
docs_x = []
docs_y = []

# -------------------
# DATA PREPARATION
# -------------------
for intent in data["intents"]:
    for pattern in intent["patterns"]:
        tokens = pattern.lower().split()
        words.extend(tokens)
        docs_x.append(tokens)
        docs_y.append(intent["tag"])

    if intent["tag"] not in labels:
        labels.append(intent["tag"])

words = sorted(set(words))
labels = sorted(labels)

training = []
output = []

out_empty = [0] * len(labels)

for i, doc in enumerate(docs_x):
    bag = []

    for w in words:
        bag.append(1 if w in doc else 0)

    output_row = out_empty[:]
    output_row[labels.index(docs_y[i])] = 1

    training.append(bag)
    output.append(output_row)

training = np.array(training)
output = np.array(output)

# -------------------
# MODEL
# -------------------
model = Sequential()
model.add(Dense(8, input_shape=(len(words),), activation='relu'))
model.add(Dense(8, activation='relu'))
model.add(Dense(len(labels), activation='softmax'))

model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

model.fit(training, output, epochs=500, batch_size=8)

model.save("model.h5")

pickle.dump(words, open("words.pkl", "wb"))
pickle.dump(labels, open("labels.pkl", "wb"))

print("Model trained successfully!")