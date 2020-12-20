from flask import Flask, render_template, request, redirect


app = Flask("SuperScrapper")


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/report")
def report():
    query_job = request.args.get("query_job")
    if query_job:
        query_job = query_job.lower()
    else:
        return redirect("/")
    return render_template("report.html", searchingBy=query_job)


app.run(host="127.0.0.1")
