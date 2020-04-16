import os
import csv
from flask import Flask, render_template, request, redirect, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
if os.path.exists("env.py"):
    import env


# instance of Flask / Flask app and we store it in the app variable
app = Flask(__name__)


app.config["MONGO_DBNNAME"] = "MyJobList"
app.config["MONGO_URI"] = "mongodb+srv://anna13:Aster1381@cluster0-rfwzk.mongodb.net/MyJobList?retryWrites=true&w=majority"


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
    return render_template("jobs.html", jobs=mongo.db.jobs.find_one({"_id": ObjectId(job_id)}))


# add job function
@app.route('/add_job')
def add_job():
    # query to list of companies
    # update retun line 42 
    # return render_template("jobs.html", jobs=mongo.db.jobs.find_one({"_id": ObjectId(job_id)}))
    return render_template("addjob.html")


@app.route('/insert_job', methods=["POST"])
def insert_job():
    requirements = request.form.get("requirements").splitlines()
    job = {
        "job_title": request.form.get("job_title"),
        "company_id": request.form.get("company_id"),
        "job_description": request.form.get("job_description"),
        "requirements": request.form.getlist("requirements"),
        "company_description": request.form.get("company_description"),
        "url": request.form.get("url")
    }
    jobs = mongo.db.jobs.insert_one(job)
    return redirect(url_for("get_jobs", job_id=jobs.inserted_id))
    # check is the company is in the db
    # if donest exis then creat new one
    # if exists then display info


@app.route('/edit_job/<job_id>', methods=["POST", "GET"])
def edit_job(job_id):
    if request.method == "GET":
        jobs = mongo.db.jobs
        the_job = mongo.db.jobs.find_one({"_id": ObjectId(job_id)})
        return render_template('editjob.html', job=the_job)
    else:
        jobs = mongo.db.jobs
        jobs.update( {'_id': ObjectId(job_id)},
    {
        "job_title": request.form.get("job_title"),
        "company_id": request.form.get("company_id"),
        "job_description": request.form.get("job_description"),
        "requirements": request.form.getlist("requirements"),
        "company_description": request.form.get("company_description"),
        "url": request.form.get("url")
    })
        return redirect(url_for('get_home'))


@app.route('/delete_job/<job_id>')
def delete_job(job_id):
    mongo.db.jobs.remove({'_id': ObjectId(job_id)})
    return redirect(url_for('get_home'))


if __name__ == "__main__":
    app.run(host=os.environ.get('IP'),
            # convert port into integer
            port=int(os.environ.get('PORT')),
            # it allows to changes to be picked up auto in the browser
            debug=True)
