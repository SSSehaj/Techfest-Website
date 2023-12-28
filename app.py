import os
from flask import Flask, render_template, url_for
# from cs50 import SQL

app = Flask(__name__)

@app.route("/")
def main():
    return render_template("main.html")

# @app.route("/wwz")
# def register():
#     return

