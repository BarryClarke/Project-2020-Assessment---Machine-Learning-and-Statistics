# See model.ipynb for development and analysis of ML models considered for this project
# The model below was chosen to be used in the Web Service 

# Numerical arrays
import numpy as np

# Data frames.
import pandas as pd

# Import required scikit learn libraries
from sklearn.model_selection import train_test_split

#Import tensorflow library required for Neural networks.
import tensorflow.keras as kr

class Predict:

    def __init__(self):
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
   
        self.model = kr.models.Sequential()
        # Change the hidden layer from 3 neurons to 5 neurons
        self.model.add(kr.layers.Dense(5, input_shape=(1,), activation='sigmoid', kernel_initializer="glorot_uniform", bias_initializer="glorot_uniform"))
        self.model.add(kr.layers.Dense(1, activation='linear', kernel_initializer="glorot_uniform", bias_initializer="glorot_uniform"))
        self.model.compile(kr.optimizers.Adam(lr=0.001), loss='mean_squared_error')

        # Fit the training dataset to the above model and run 5000 epochs in batches of 10 at a time.
        self.model.fit(X_train, y_train, epochs=5, batch_size=10)
    
    def calc(self, speed):
        Speed = float(speed)
        prediction = str('%.2f' %(self.model.predict([Speed])))
        print("Predicted Power: ", prediction)
        
        return prediction
    
power1 = Predict()