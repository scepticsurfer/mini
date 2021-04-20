# Entry point for the application.
from . import app    # For application discovery by the 'flask' command.
#from . import views  # For import side-effects of setting up routes.

from datetime import datetime
from flask import Flask, render_template
from . import app

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/company/company/")
def company():
    return render_template("company/company.html")

@app.route("/contacts/feedback/")
def contact():
    return render_template("contacts/feedback.html")