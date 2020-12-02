from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def index():
    return "Home page"



#@app.route("/api/v1.0/precipitation")
#def precipitation():


#@app.route("/api/v1.0/stations")
#def stations():

#@app.route("/api/v1.0/tobs")
#def tobs():

#@app.route("/api/v1.0/<start>")
#def start():

#@app.route("/api/v1.0/<start>/<end>")
#def end():




#if __name__ == "__main__":
    #app.run(debug=True)
