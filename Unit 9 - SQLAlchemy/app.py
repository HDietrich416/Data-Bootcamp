# Import Dependencies
import datetime as dt
import numpy as np
import pandas as pd

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func 

from flask import Flask, jsonify

#SQLAlchemy 

engine = create_engine('sqlite:///Resources/hawaii.sqlite')
Base = automap_base
Base.prepare(engine, reflect=True)
Measurement = Base.classes.Measurement
Station = Base.classes.station

#Flask
app = Flask(__name__)

@app.route("/")
def home():
    return "Welcome"
    return"Available Routes:"
    return"/api/v1.0/precipitation"
    return"/api/v1.0/stations"
    return"/api/v1.0/tobs"
    return"/api/v1.0/<start>"
    return"/api/v1.0/<start>/<end>"


@app.route("/api/v1.0/precipitation")
def precipitation():
    last_date = dt.datetime(2017, 8, 23)
    first_date = last_date - timedelta(days=364)
    session = Session(engine)
    results = session.query(Measurement.date, Measurement.prcp)\
                .filter(Measurement.date >=first_date)\
                .group_by(Measurement.date).all()
    session.close()

    for date, prcp in results:
        measurement_dict ={}
        measurement_dict['date'] = date
        measurement_dict['prcp'] = prcp
        all_measurment.append(measurement_dict)

    return jsonify(all_measurement)

@app.route("/api/v1.0/stations")
def stations(): 
    session = Session(engine)
    results = session.query(Measurement.station).group_by(Measurement.station).all()
    session.close()

    return jsonify(results)


#@app.route("/api/v1.0/tobs")

#@app.route("/api/v1.0/<start>")

#@app.route("/api/v1.0/<start>/<end>")

if __name__ =='main':
    app.run(debug=True)






