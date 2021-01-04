# flask for web app.
import flask as fl
# numpy for numerical work.
import numpy as np

# Create a new web app.
app = fl.Flask(__name__)

# Add root route.
@app.route("/")
def home():
  return app.send_static_file('index.html')

# Add uniform route.
@app.route('/api/predict')
def predict(speed):
  return {"value": np.random.uniform()}
