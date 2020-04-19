import os
from flask import Flask, render_template, request, redirect, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
if os.path.exists("env.py"):
    import env


app = Flask(__name__)


app.config["MONGO_DBNNAME"] = "MyJobList"
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")


mongo = PyMongo(app)


@app.route('/')
@app.route('/get_home')
def get_home():
    print("home page")
    return render_template("index.html", jobs=mongo.db.jobs.find())


@app.route('/get_jobs/<job_id>')
def get_jobs(job_id):
    print("some job")
    return render_template("jobs.html",
                           jobs=mongo.db.jobs.find_one({"_id":
                                                       ObjectId(job_id)}))


@app.route('/add_job')
def add_job():
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


@app.route('/edit_job/<job_id>', methods=["POST", "GET"])
def edit_job(job_id):
    if request.method == "GET":
        jobs = mongo.db.jobs
        the_job = mongo.db.jobs.find_one({"_id": ObjectId(job_id)})
        return render_template('editjob.html', job=the_job)
    else:
        jobs = mongo.db.jobs
        jobs.update({'_id': ObjectId(job_id)},
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
            port=int(os.environ.get('PORT')),
            # it allows to changes to be picked up auto in the browser
            debug=False)
