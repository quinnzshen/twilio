from flask import Flask, request, redirect
from twilio.rest import TwilioRestClient
import twilio.twiml
import os

# Your Account Sid and Auth Token from twilio.com/user/account
account_sid = "ACbfc75796ba5579685950fd207df57f40"
auth_token  = "7076029eafcdbccba175309a50eccda3"

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def hello():
    """Display texted message."""
    # body = request.values.get('Body', None)
    client = TwilioRestClient(account_sid, auth_token)

    messages = client.messages.list()
    last_message = messages[len(messages) - 1]

    response = ""
    response += "From: " + last_message.from_ + "\n"
    response += "To: " + last_message.to + "\n"
    response += "Body: " + last_message.body

    resp = twilio.twiml.Response()
    resp.message(response)

    return str(resp)

if __name__ == "__main__":
    app.run()