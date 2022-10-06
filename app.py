from flask import Flask, render_template, request, redirect, url_for, session

import re


app = Flask(__name__)


@app.route("/")
@app.route("/login")
def login():
    return render_template("login.html")


@app.route("/register")
def register():
    return render_template("register.html")


@app.route("/home")
def home():
    return render_template("index.html")
