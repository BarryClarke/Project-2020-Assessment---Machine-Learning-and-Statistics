# <div align="center">Final Project - Machine Learning and Statistics 20-21 52954</div>
# <div align="center">Author - Barry Clarke</div>
# <div align="center">Student Number: G00376293 [1]</div>


Repository for the final project within Machine Learning and Statistics module

## Scope
1. Given a dataset of wind speed and corresponding Power generated by a wind turbine, use Machine Learning to train a model of the dataset. Analyse and discuss the accuracy of the model.
2. Based on the model, create a Web service that accurately predicts wind turbine power output from wind speed values
3. Provide a Dockerfile to build and run the web service in a container.

## Description
This project encompasses Machine Learning and hosting a web service so that the benefits of the modelling can be availed of by those permitted. The repository consists of the following files:
1. A Jupyter notebook: The dataset (powerproduction.txt) is read in from the Data folder and provisionally analysed to get familiar with its contents. Some major outliers were observed, so some data pre-processing was completed in order to have a more consistent dataset for modelling. The numpy polyfit function was applied to the dataset and it was found that a 5th degree polynomial function could quite accurately characterise the data. Using this knowledge, the machine learning regression tools from the scikit lear package in python were used to train a model, and then test this model with a some of the dataset held back for testing. Following this, the newer machine learning approach of neural networks was introduced and applied to train the dataset. As this was a first run at neural networks for me, 5 different neural networks were built, using tensorflow and keras, and ran. It was observed that there was very little difference in the accuracy of all 5. Please note the run time of this notebook has significant due to 5 neural networks, however I felt it was a worthwhile exercise for my first incursion into neural networks, so I have retaned all 5 networks in the notebok. It was observed that the accuracy of the neural networks (R-Squared  ~ 0.991) was better than the scikit learn (R-Squared = 0.988).

To view the source code in jupyter notebook, please follow the below instructions:
1. In this repoistory (ie Project-2020-Assessment---Machine-Learning-and-Statistics) click on the clone or download button and copy the URL
2. In cmder/command prompt on your system, clone the repository using the command git clone followed by paste the URL
3. Go to the directory where you saved cloned the Repository
4. Type "jupyter notebook" for the repository to open in jupyter
5. When Jupyter notebook opens, model.ipynb file
6. In this file, locate the *Kernal* tab and select *Restart & Run All* <br>
**Note:** This assumes you have python and Github setup on your machine.<br>


2. Using the analysis from the jupyter notebook, one of the neural networks was written into a python script (model.py) which was imported into predict.py, a Flask server used for crewting a web service. This web service simply uses the model to predict an expected power generated from the wind turbine with a user inputted wind speed value.<br><br>

To view the source code contained within Predict.py and model.py, open visual Studio Code or Notepad++, locate the above directory where you have cloned the repository and select model.py and predict.py.<br><br>

To run the seb service, open the cmd or cmder prompt, navigate to the above folder once again, and type the following commands<br><br>
    
set FLASK_APP=rando.py<br><br>
    
python -m flask run<br><br>

You should see the Flask server start, following by the neural network initialise. This neural network consists of 5000 epochs, so it takes a number of minutes to run though the model. Once the model has been trained, the command prompt will show the http://127.0.0.1:5000/ address. Copy this, open your web browser and paste into the location bar. The web service should appear. Using this web service, input values for windspeed and click Predict power. A power prediction based on the model trained will appear.

The web service can also be run in a virtual environment. In this case, requirements.txt file contains all the necessary packages to allow the web service operate. These will need to be installed in the vitrual environment.






