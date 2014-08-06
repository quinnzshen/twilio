from flask import Flask, request, redirect
import twilio.twiml
import os

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def hello():
    """Display texted message."""
    body = request.values.get('Body', None)

    resp = twilio.twiml.Response()
    resp.message(body)

    return str(resp)

if __name__ == "__main__":
    app.run()