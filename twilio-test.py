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
    # resp.say("Hello Monkey")
    # resp.play("http://demo.twilio.com/hellomonkey/monkey.mp3")
    resp.play("""https://s3.amazonaws.com/quinnzshen/Dial+34.mp3?X-Amz-Date=20140806T234301Z&X-Amz-Expires=300&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Signature=6393ff82e649627120d987986ee1e0ef21f87d0864144e7a080264d4be4d1f89&X-Amz-Credential=ASIAIWX5UFQEGASD6RWQ/20140806/us-east-1/s3/aws4_request&X-Amz-SignedHeaders=Host&x-amz-security-token=AQoDYXdzELH//////////wEawAK74iApvEU5L/Q9eecJo8iYOi02Odnw7cuCWTyC5DyrYb8YRbQi6iEdUlfFm9wpLy1ImocHemWmacYDkekjUC4zsNIjMjSlNHGmsUSx4WIFXAEWZwjwYd0WLzNHuFAotcHhvsrQZzLCI1oytZlArGhP%2BZK3KeGlqMN356lSgbDyg4SNWNJCTp0rZL5Cf1g5eYJWYama0ioon34prC7DSjTJzOhk1H2uqWduzi%2Bb5I8m054OB3XSocevMqNvRRy%2BxL97ZHc56qFe5%2BEiFiFt2mCgsyu4iPKjiYt2p3VyxaOTAc1gNgBY8T7BJSfuzqy3E5f1CrtrNISdtU0zviZbYsC7WJnPD2iiVhDZ8Xkl2G01hbdDKqpgkVFGb8c7E/MvatsOahU0RE8QEtNUcBjd1kfVTe9PkV9MoBsNPB2kkaNp4iDE%2BoqfBQ%3D%3D""")
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