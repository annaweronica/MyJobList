import os
import csv
from flask import Flask, render_template, request, redirect, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from os import path
if path.exists("env.py"):
    import env



# instance of Flask / Flask app and we store it in the app variable
app = Flask(__name__)



app.config["MONGO_DBNNAME"] = "MyJobList"
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")


# an instance of PyMongo and add app into that with constructor method
# app object as argument
mongo = PyMongo(app)


@app.route('/')
# function with a decorator which includes route to that function
@app.route('/get_home')
def get_home():
    print("home page")
    return render_template("index.html", jobs=mongo.db.jobs.find())


# view job details page
@app.route('/get_jobs/<job_id>')
def get_jobs(job_id):
    print("some job")
    return render_template("view-job.html", jobs=mongo.db.jobs.find_one({"_id": ObjectId(job_id)}))


@app.route('/import_data')
def import_data():
    csvfile = open('data/dbExcel-ex.csv', 'r')
    reader = csv.DictReader( csvfile )
    header= ["job_title", "company_id", "job_description", "company_description", "url"]

    for each in reader:
        row={}
        for field in header:
            row[field]=each[field]

        mongo.db.jobs.insert_one(row)
    return "hello Wrold"


if __name__ == "__main__":
    app.run(host=os.environ.get('IP'),
            # convert port into integer
            port=int(os.environ.get('PORT')),
            # it allows to changes to be picked up auto in the browser
            debug=True)
