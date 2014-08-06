import twilio
from twilio.rest import TwilioRestClient
 
# Your Account Sid and Auth Token from twilio.com/user/account
account_sid = "ACbfc75796ba5579685950fd207df57f40"
auth_token  = "7076029eafcdbccba175309a50eccda3"
 
try:
    client = TwilioRestClient(account_sid, auth_token)
 
    message = client.messages.create(
        body="Hello World",
        to="+13016137169",    # User Phone Number
        from_="+12405475057"  # Twilio Number
    )

    print message.sid
except twilio.TwilioRestException as e:
    print e