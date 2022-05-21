{
 "cells": [],
 "metadata": {},
 "nbformat": 4,
 "nbformat_minor": 5
}
# 1. import Flask
from unittest import result
import numpy as np

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify

# 2. Create an app, being sure to pass __name__
app = Flask(__name__)


# 3. Define what to do when a user hits the index route
@app.route("/")
def home():
     return (
        f"/api/v1.0/precipitation"
        f"/api/v1.0/stations"
        f"/api/v1.0/tobs"
        f"/api/v1.0/<start>"
        
    )


# 4. Define what to do when a user hits the /about route
#`/api/v1.0/precipitation`

 # * Convert the query results to a dictionary using `date` as the key and `prcp` as the value.

 # * Return the JSON representation of your dictionary.

@app.route("/api/v1.0/precipitation")
def precipitation():
    session = Session(engine)

    results = session.query(measurement.date, measurement.prcp).all()
    session.close()

    all_data = []
    for date, prcp in results:
        data_dict = {}
        data_dict["date"] = date
        data_dict["prpc"] = prpc
        
        all_data.append(data_dict)

    return jsonify(all_data)
    

@app.route("/api/v1.0/stations")
def stations():
    session = Session(engine)
    

    

    session.close()

    

   

@app.route("/api/v1.0/tobs")
def tobs():
    session = Session(engine)
    

@app.route("/api/v1.0/<start>")
def start():
    session = Session(engine)
  



if __name__ == "__main__":
    app.run(debug=True)
