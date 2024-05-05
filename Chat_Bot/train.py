# libraries
import random
from tensorflow.keras.optimizers import SGD
from keras.layers import Dense, Dropout
from keras.models import Sequential
import numpy as np
import pickle
import json
import nltk
from nltk.stem import WordNetLemmatizer
lemmatizer = WordNetLemmatizer()
nltk.download('omw-1.4')
nltk.download("punkt")
nltk.download("wordnet")

# Initialize empty lists and dictionaries
words = []
classes = []
documents = []
ignore_words = ["?", "!"]
data_file = open("intents.json").read()
intents = json.loads(data_file)

# Extract words and intents from intents.json
for intent in intents["intents"]:
    for pattern in intent["patterns"]:
        # Tokenize and add words to the list
        w = nltk.word_tokenize(pattern)
        words.extend(w)
        # Add documents as tuples of words and intents
        documents.append((w, intent["tag"]))
        # Add unique intents to the list
        if intent["tag"] not in classes:
            classes.append(intent["tag"])

# Lemmatize and remove duplicates from words
words = [lemmatizer.lemmatize(w.lower()) for w in words if w not in ignore_words]
words = sorted(list(set(words)))
classes = sorted(list(set(classes)))

print(len(documents), "documents")
print(len(classes), "classes", classes)
print(len(words), "unique lemmatized words", words)

# Save words and classes to pickle files
pickle.dump(words, open("words.pkl", "wb"))
pickle.dump(classes, open("classes.pkl", "wb"))

# Initialize training data
training = []

# Loop through documents to create training data
for doc in documents:
    # Initialize bag of words for current document
    bag = []
    
    # Tokenize and lemmatize words in the pattern
    pattern_words = [lemmatizer.lemmatize(word.lower()) for word in doc[0]]
    
    # Create bag of words with 1 if word is in pattern_words, else 0
    for word in words:
        bag.append(1) if word in pattern_words else bag.append(0)

    # Initialize output row with all zeros
    output_row = [0] * len(classes)
    
    # Set 1 at index corresponding to current intent
    output_row[classes.index(doc[1])] = 1

    # Append current bag of words and output row to training data
    training.append([bag, output_row])

# Shuffle training data
random.shuffle(training)

# Convert training data to NumPy array
training = np.array(training)

# Split training data into input (X) and output (Y)
train_x = list(training[:, 0])
train_y = list(training[:, 1])

# Create and compile model
model = Sequential()
model.add(Dense(128, input_shape=(len(train_x[0]),), activation="relu"))
model.add(Dropout(0.5))
model.add(Dense(64, activation="relu"))
model.add(Dropout(0.5))
model.add(Dense(len(train_y[0]), activation="softmax"))
model.summary()

sgd = SGD(lr=0.01, decay=1e-6, momentum=0.9, nesterov=True)
model.compile(loss="categorical_crossentropy", optimizer=sgd, metrics=["accuracy"])

# Train model
hist = model.fit(np.array(train_x), np.array(train_y), epochs=200, batch_size=5, verbose=1)

# Save model
model.save("chatbot_model.h5", hist)
print("model created")
