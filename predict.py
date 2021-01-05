# flask for web app.
import flask as fl
# numpy for numerical work.
import numpy as np

#from flask import jsonify

# Data frames.
import pandas as pd

# Import required scikit learn libraries
from sklearn.model_selection import train_test_split

#Import tensorflow library required for Neural networks.
import tensorflow.keras as kr

# Create a new web app.
app = fl.Flask(__name__)

# Add root route.
@app.route("/")
def home():
  return app.send_static_file('index.html')

# Read in the powerproduction dataset from the Data folder in the repository. Although it is a text file, we can read it in as a csv file, such is the format of the data contained within.
data = pd.read_csv('Data/powerproduction.txt')

df = pd.DataFrame(data)

# delete any rows from the dataset where a zero Power output is recorded
df = df[df.power != 0]

# Select the columns of the DataFrame
Speed = df['speed']
Power = df["power"]

# Convert to arrays
x = Speed.to_numpy()
y = Power.to_numpy()

# Prepare the dataset for training and testing
data = df.values
# split into inpiut and output elements
X, y = data[:, :-1], data[:, -1]
# split into train and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=1)

# Build a model using Keras
model = kr.models.Sequential()
# Change the hidden layer from 3 neurons to 5 neurons
model.add(kr.layers.Dense(5, input_shape=(1,), activation='sigmoid', kernel_initializer="glorot_uniform", bias_initializer="glorot_uniform"))
model.add(kr.layers.Dense(1, activation='linear', kernel_initializer="glorot_uniform", bias_initializer="glorot_uniform"))
model.compile(kr.optimizers.Adam(lr=0.001), loss='mean_squared_error')

# Fit the training dataset to the above model and run 5000 epochs in batches of 10 at a time.
model.fit(X_train, y_train, epochs=50, batch_size=10)
#power = model.predict([20])
#print("power: ", (power))

import json
from json import JSONEncoder




#print("Printing JSON serialized NumPy array")
#print(encodedNumpyData)


# Add uniform route.
@app.route('/api/predict/<float:speed>')
def predict(speed):
  power1 = model.predict([speed])
  #https://pynative.com/python-serialize-numpy-ndarray-into-json/
  class NumpyArrayEncoder(JSONEncoder):
    def default(self, obj):
        if isinstance(obj, np.ndarray):
            return obj.tolist()
        return JSONEncoder.default(self, obj)
  # Serialization
  numpyData = {"array": power}
  encodedNumpyData = json.dumps(numpyData, cls=NumpyArrayEncoder)  # use dump() to write array into file



  return encodedNumpyData
  #return {"value": np.random.uniform()}
