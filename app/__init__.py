from flask import Flask

# setup objects
app = Flask(__name__)

# our views
from app import routes # noQA
