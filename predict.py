# flask for web app.
import flask as fl
# numpy for numerical work.
import numpy as np
# jsonify for HTTP comms
from flask import jsonify

# Import an instance of a class for the model, contained in model.py
from model import power1

# Create a new web app.
app = fl.Flask(__name__)

# Add root route.
@app.route("/")
def home():
  return app.send_static_file('index.html')

# Add uniform route.
@app.route('/api/predict/<string:speed>')
def power(speed):
  return jsonify(power1.calc(speed))

if __name__=="__main__":
  app.run(debug=False)