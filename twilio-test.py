from flask import Flask, request, redirect
import twilio.twiml
import os

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def hello():
    return "Hello World!"

if __name__ == "__main__":
    app.run()