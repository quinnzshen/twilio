from flask import Flask, request, redirect
import twilio.twiml
import os

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def hello():
    """Display texted message."""

    return request.values

if __name__ == "__main__":
    app.run()