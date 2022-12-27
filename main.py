from flask import Flask, request, render_template

from helpers import get_date_and_time

app = Flask(__name__, template_folder="templates")


@app.route("/")
def homepage():
    return render_template("index.html")


@app.route("/data")
def data():
    timezone = request.args.get("timezone")
    return (
        get_date_and_time(timezone=timezone)
        if timezone
        else {"ok": "error", "error": "No timezone provided"}
    )
