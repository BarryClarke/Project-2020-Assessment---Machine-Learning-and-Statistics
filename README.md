![Web-Service](Images/WebService.JPG)

## <div align="center">Final Project - Machine Learning and Statistics 20-21 52954</div>
## <div align="center">Author - Barry Clarke</div>
## <div align="center">Student Number: G00376293</div>

Repository for the final project within Machine Learning and Statistics module

## Scope
1. Given a dataset of wind speed and corresponding Power generated by a wind turbine, use Machine Learning to train a model of the dataset. Analyse and discuss the accuracy of the model.
2. Based on the model, create a Web service that accurately predicts wind turbine power output from wind speed values
3. Provide a Dockerfile to build and run the web service in a container.

## Description
This project encompasses Machine Learning and hosting a web service so that the benefits of the modelling can be availed of by general, non technical users. The repository consists of the following files:

### model.ipynb
A Jupyter notebook: The dataset (powerproduction.txt) is read in from the Data folder and provisionally analysed to get familiar with its contents. Some major outliers were observed, so some data pre-processing was completed in order to have a more consistent dataset for modelling. The numpy polyfit function was applied to the dataset and it was found that a 5th degree polynomial function could quite accurately characterise the data. Using this knowledge, the machine learning regression tools from the scikit learn package in python were used to train a model, and then test this model with a some of the dataset held back for testing. Following this, the newer machine learning approach of neural networks was introduced and applied to train the dataset. As this was a first run at neural networks for me, 5 different neural networks were built, using tensorflow and keras, and ran. It was observed that there was very little difference in the accuracy of all 5. Please note the run time of this notebook is significant due to 5 neural networks, however I felt it was a worthwhile exercise for my first incursion into neural networks, so I have retained all 5 networks in the notebok. It was observed that the accuracy of the neural networks (R-Squared  ~ 0.991) was better than the scikit learn (R-Squared = 0.988).

If viewing through Github, the ipynb file is best viewed through nbviewer, as certain text formatting will not load correctly when viewing through GitHub. Please follow this link to view the notebook in nbviewer  [model.ipynb](https://nbviewer.jupyter.org/github/BarryClarke/Project-2020-Assessment---Machine-Learning-and-Statistics/blob/main/model.ipynb)

To view the source code in jupyter notebook, please follow the below instructions:
1. In this repoistory (ie Project-2020-Assessment---Machine-Learning-and-Statistics) click on the clone or download button and copy the URL
2. In cmder/command prompt on your system, clone the repository using the command git clone followed by paste the URL
3. Go to the directory where you saved the cloned Repository
4. Type "jupyter notebook" for the repository to open in jupyter
5. When Jupyter notebook opens, model.ipynb file
6. In this file, locate the *Kernal* tab and select *Restart & Run All* <br>
**Note:** This assumes you have python and Github setup on your machine.<br>

### predict.py and model.py
Using the analysis from the jupyter notebook, one of the neural networks was written into a python script (model.py) which was imported into predict.py, a Flask server used for creating a web service. This web service uses the model to predict an expected power generated from the wind turbine with a user inputted wind speed value. I have seperated  the model script from the server script, and imported an instance of the class of the model, as I found this the cleanest way to do this.<br>

To view the source code contained within Predict.py and model.py, open visual Studio Code or Notepad++, locate the above directory where you have cloned the repository and select model.py and predict.py.<br>

### Web service
#### On Windows
To run the web service, open the cmd or cmder prompt, navigate to the directory where you saved the cloned repository, and type the following commands<br>
   
set FLASK_APP=predict.py<br>
    
python -m flask run<br>

You should see the Flask server start, following by the neural network initialise. This neural network consists of 5000 epochs, so it takes a number of minutes to run though the training of the model. Once the model has been trained, the command prompt will show the http://127.0.0.1:5000/ address. Copy this, open your web browser and paste into the location bar. The web service should appear. Using this web service, input values for windspeed and click Predict power. A power prediction based on the model trained will appear.

#### In a virtual Environmet
The web service can also be run in a virtual environment. In this case, requirements.txt file contains all the necessary packages to allow the web service operate. These will need to be installed in the vitrual environment. Once a vitrual environment is created and the contents of the requirements.txt installed, the virtual environment can be used to run the web service. To to this, from the directory where you saved the cloned Repository type the followong commands<br>

.\venv\Scripts\activate.bat<br>

python predict.py<br>

You should see the neural network initialise, and the Flask app "predict" start. Once again, this neural network consists of 5000 epochs, so it takes a number of minutes to run though the model. Once the model has been trained and the Flask app started, the command prompt will show the http://127.0.0.1:5000/ address. Copy this, open your web browser and paste into the location bar. The web service should appear. Using this web service, input values for windspeed and click Predict power. A power prediction based on the model trained will appear.

#### On Docker
Finally, the web service is capable of running on Docker. To run the web service on docker, navigate to the directory where you saved the cloned Repository once again, and type the following commands<br>

docker build -t predict-app .<br>

docker run -d -p 5000:5000 predict-app<br>

After the first command, it may time some time to build a container for the web service. Once built, the second command will run the web service, which can be viewed at http://127.0.0.1:5000/

## References
In creating this repository, the below references were used<br>
1. https://en.wikipedia.org/wiki/Wind_turbine_design#Design_specification
2. https://towardsdatascience.com/ways-to-detect-and-remove-the-outliers-404d16608dba 
3. https://github.com/ianmcloughlin/jupyter-teaching-notebooks/blob/master/regression.ipynb
4. https://en.wikipedia.org/wiki/Least_squares
5. https://numpy.org/doc/stable/reference/generated/numpy.polyfit.html
6. https://scikit-learn.org/
7. https://towardsdatascience.com/machine-learning-basics-polynomial-regression-3f9dd30223d1
8. https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LinearRegression.html
9. https://statisticsbyjim.com/glossary/ordinary-least-squares/
10. https://statisticsbyjim.com/regression/interpret-r-squared-regression/
11. https://towardsdatascience.com/r-squared-recipe-5814995fa39a
12. https://en.wikipedia.org/wiki/Gradient_descent
13. https://www.tensorflow.org/tutorials
14. https://www.tensorflow.org/api_docs/python/tf/keras/initializers/GlorotUniform
15. https://keras.io/api/optimizers/adam/
16. https://stackoverflow.com/questions/1321878/how-to-prevent-favicon-ico-requests
17. https://stackoverflow.com/questions/39579666/how-to-set-background-image-on-flask-templates/39579810
18. https://getbootstrap.com/docs/5.0/forms/form-control/
19. https://www.w3schools.com/jquery/jquery_dom_get.asp
20. https://learnonline.gmit.ie/course/view.php?id=1121






