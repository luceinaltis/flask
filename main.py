from flask import Flask, render_template, request, redirect, send_file
from scraper import get_jobs
from exporter import save_to_file

app = Flask("SuperScrapper")

db = {}


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/report")
def report():
    query_job = request.args.get("query_job")
    if query_job:
        query_job = query_job.lower()
        if db.get(query_job):
            jobs = db.get(query_job)
        else:
            jobs = get_jobs(query_job)
            db[query_job] = jobs

    else:
        return redirect("/")
    return render_template("report.html", searchingBy=query_job, searchingNum=len(jobs), jobs=jobs)


@app.route("/export")
def export():
    try:
        word = request.args.get("query_job")
        if not word:
            raise Exception()
        word = word.lower()
        jobs = db.get(word)
        if not jobs:
            raise Exception()
        save_to_file(jobs)
        return send_file("jobs.csv")
    except:
        return redirect("/")


app.run(host="127.0.0.1")
