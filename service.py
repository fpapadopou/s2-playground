from flask import Flask

# Create flask app
app = Flask(__name__)


@app.route("/")
def index():
    return "Whazza!"
