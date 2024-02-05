# Import the dependencies.
import numpy as np

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify



#################################################
# Database Setup
#################################################
# Create engine using the `hawaii.sqlite` database file

engine = create_engine("sqlite:///Resources/hawaii.sqlite")

# Declare a Base using `automap_base()`
Base = automap_base()

# Use the Base class to reflect the database tables
Base.prepare(autoload_with=engine)

# Assign the measurement class to a variable called `Measurement` and
# the station class to a variable called `Station`
Station = Base.classes.station
Measurement = Base.classes.measurement

# Create a session
session = Session(engine)

#################################################
# Flask Setup
#################################################
app = Flask(__name__)



#################################################
# Flask Routes
#################################################

@app.route("/")
def welcome():
    """List all available api routes."""
    return (
        f"Available Routes:<br/>"
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/stations<br/>"
        f"/api/v1.0/tobs<br/>"
        f"/api/v1.0/<start><br/>"
        f"/api/v1.0/<start>/<end>"
    )

@app.route("/api/v1.0/precipitation")
def precipitation():
    # Create our session (link) from Python to the DB
    session = Session(engine)

    """Return a list of all passenger names"""
    # Query all passengers
    precip = session.query(Measurement.prcp).all()

    session.close()

    # Convert list of tuples into normal list
    all_names = list(np.ravel(precip))

    return jsonify(all_names)

@app.route("/api/v1.0/stations")
def stations():
        # Create our session (link) from Python to the DB
    session = Session(engine)

    """Return a list of all passenger names"""
    # Query all Stations
    stati = session.query(Station.station).all()

    session.close()

    # Convert list of tuples into normal list
    all_stations = list(np.ravel(stati))

    return jsonify(all_stations)

@app.route("/api/v1.0/tobs")
def temperature():
        # Create our session (link) from Python to the DB
    session = Session(engine)

    """Return a list of all passenger names"""
    # Query all Stations
    temp = session.query(Measurement.tobs).all()

    session.close()

    # Convert list of tuples into normal list
    all_temp = list(np.ravel(temp))

    return jsonify(all_temp)

@app.route("/api/v1.0/<start>")
def date_start():
        # Create our session (link) from Python to the DB
    session = Session(engine)

    """Return a list of all passenger names"""
    # Query all Stations
    start_date = session.query(Measurement.date).all()

    session.close()

    # Convert list of tuples into normal list
    all_start = list(np.ravel(start_date))

    return jsonify(all_start)

@app.route("/api/v1.0/<start>/<end>")
def date_end():
        # Create our session (link) from Python to the DB
    session = Session(engine)

    """Return a list of all passenger names"""
    # Query all Stations
    end_date = session.query(Measurement.date).all()

    session.close()

    # Convert list of tuples into normal list
    all_end = list(np.ravel(end_date))

    return jsonify(all_end)

if __name__ == '__main__':
    app.run(debug=True)
