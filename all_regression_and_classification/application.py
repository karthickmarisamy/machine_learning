import pickle
from flask import Flask, request, jsonify, render_template
import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler

application = Flask(__name__)
app = application

@app.get('/')
def index():
    return "success"

if __name__ == '__main__':
    app.run()