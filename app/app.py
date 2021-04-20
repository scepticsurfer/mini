# Entry point for the application.
from . import app
from datetime import datetime
from flask import Flask, render_template

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/company/company/")
def company():
    return render_template("company/company.html")

@app.route("/contacts/feedback/")
def contact():
    return render_template("contacts/feedback.html")