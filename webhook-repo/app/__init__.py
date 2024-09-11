from flask import Flask
from flask_pymongo import PyMongo
from app.webhook.routes import webhook  # Importing the webhook blueprint

# MongoDB setup
mongo = PyMongo()

# Creating the Flask app
def create_app():
    app = Flask(__name__)

    # MongoDB configuration (adjust URI as needed)
    app.config["MONGO_URI"] = "mongodb://localhost:27017/webhookdb"  

    # Initialize MongoDB connection
    mongo.init_app(app)

    # Registering the webhook blueprint
    app.register_blueprint(webhook)

    return app
