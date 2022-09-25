
from flask import Flask, render_template, request, make_response
import sqlite3
 

HOST_NAME = "0.0.0.0"
HOST_PORT = 5000
DBFILE = "patients.db"
app = Flask(__name__)


def getpatients():
  conn = sqlite3.connect(DBFILE)
  cursor = conn.cursor()
  cursor.execute("SELECT * FROM `patients`")
  results = cursor.fetchall()
  conn.close()
  return results

@app.route("/patients")
def index():
  patients = getpatients()
  return render_template("patients_table.html", patients=patients)

if __name__ == "__main__":
  app.run(HOST_NAME, HOST_PORT)
  
