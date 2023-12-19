from flask import Flask
from config import Config


# create install of class, by pass _name_ parameter
app = Flask(__name__)

# setting properties for instance app
app.config.from_object(Config)

from app import routes