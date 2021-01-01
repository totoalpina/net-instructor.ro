from flask import Flask
from application import app

@app.route('/')
def index():
    return "<h1>hello net-instructor.ro</h1>"