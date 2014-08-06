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

    "Do nothing but log"

    resp = twilio.twiml.Response()
    resp.say("Hello Monkey")
    resp.play("http://demo.twilio.com/hellomonkey/monkey.mp3")
    # resp.play("""https://dl-web.dropbox.com/get/Nokia/Dial%2034.mp3?_subject_uid=68290986&w=AABk-yLVCNEdnXuytj5qZ2mOE1dbmurUwr2RyLhZyn7lSA""")
    # client = TwilioRestClient(account_sid, auth_token)

    # message = client.messages.create(
    #     body=request.values.get('Body', None),
    #     to="+13016137169",    # User Phone Number
    #     from_="+12405475057"  # Twilio Number
    # )
    # messages = client.messages.list()
    # last_message = messages[0]

    # response = ""
    # response += "From: " + last_message.from_ + "\n"
    # response += "To: " + last_message.to + "\n"
    # response += "Body: " + last_message.body

    # resp = twilio.twiml.Response()
    # resp.message(response)

    return str(resp)

if __name__ == "__main__":
    app.run()