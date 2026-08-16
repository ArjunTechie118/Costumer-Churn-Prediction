from flask import Flask 
from src.logger import logging
from src.exception import CostumException
import os,sys

app = Flask(__name__)

@app.route('/',methods=['GET','PUSH'])
def index():
    try:
        raise Exception("I am testing my costum file")
    except Exception as e:
        abc = CostumException(e,sys)
        logging.info(abc.error_message)
        return "Welcom to Customer Churn Prediction"

if __name__ == "__main__":
    app.run(debug=True)