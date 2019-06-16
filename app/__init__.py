from flask import Flask

app = Flask(__name__)

# from app import routes #noQA

app.config.setdefault('FREEZER_DESTINATION', '../docs')

