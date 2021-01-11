# Import Dependencies
import datetime as dt
from datetime import timedelta
import numpy as np
import pandas as pd


import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func 

from flask import Flask, jsonify

#SQLAlchemy 

engine = create_engine('sqlite:///Unit 9 - SQLAlchemy/Resources/hawaii.sqlite')
Base = automap_base()
Base.prepare(engine, reflect=True)

# Save references to each table
Measurement = Base.classes.measurement
Station = Base.classes.station

#Flask
app = Flask(__name__)

@app.route("/")
def home():
    return (
        f"Welcome! <br/>"
        f"Here are the available routes: <br/>"
        f"/api/v1.0/precipitation <br/>"
        f"/api/v1.0/stations <br/>"
        f"/api/v1.0/tobs <br/>"
        f"/api/v1.0/start <br/>"
        f"/api/v1.0/start/end"
    )
   
@app.route("/api/v1.0/precipitation")
def precipitation():
    last_date = dt.datetime(2017, 8, 23)
    first_date = last_date - timedelta(days=365)
    session = Session(engine)
    results = session.query(Measurement.date, Measurement.prcp).\
                filter(Measurement.date >=first_date)\
                .group_by(Measurement.date).all()
    session.close()

    all_measurement = []
    for date, prcp in results:
        measurement_dict ={}
        measurement_dict['date'] = date
        measurement_dict['prcp'] = prcp
        all_measurement.append(measurement_dict)

    return jsonify(all_measurement)

@app.route("/api/v1.0/stations")
def stations(): 
    session = Session(engine)
    results = session.query(Measurement.station).group_by(Measurement.station).all()
    session.close()

    return jsonify(results)


@app.route("/api/v1.0/tobs")
def tobs():
    last_date = dt.datetime(2017, 8, 23)
    first_date = last_date - timedelta(days=365)
    session = Session(engine)
    tobs_results = session.query(Measurement.date, Measurement.tobs)\
                     .filter(Measurement.station == "USC00519281")\
                    .filter(Measurement.date >=first_date).all()
    session.close()

    all_tobs = []
    for date, tobs in tobs_results:
        tobs_dict ={}
        tobs_dict['date'] = date
        tobs_dict['tobs'] = tobs
        all_tobs.append(tobs_dict)

    return jsonify(all_tobs)


@app.route("/api/v1.0/<start>")
@app.route("/api/v1.0/<start>/<end>")
def stats(start=None, end=None):
    session = Session(engine)

    sel = [func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)]
    
    if not end:
        results = session.query(*sel).filter(Measurement.date >= start).all()

        temps = list(np.ravel(results))
        
        return jsonify(temps)

    results = session.query(*sel).filter(Measurement.date >= start).\
        filter(Measurement.date >= start).\
        filter(Measurement.date <= end).all()

    temps = list(np.ravel(results))
    return jsonify(temps)
    session.close()


if __name__ =='__main__':
    app.run(debug=True)






