import twilio
from twilio.rest import TwilioRestClient
from time import sleep
 
# Your Account Sid and Auth Token from twilio.com/user/account
account_sid = "ACbfc75796ba5579685950fd207df57f40"
auth_token  = "7076029eafcdbccba175309a50eccda3"

try:
    client = TwilioRestClient(account_sid, auth_token)
    messages = client.messages.list()
    size = len(messages)

    while True:
        messages = client.messages.list()
        if size != len(messages):
            new_message = messages[0]

            print "New message!\n-----"
            response = "From: " + new_message.from_ + "\n"
            response += "Body: " + new_message.body + "\n"
            print response

            size = len(messages)
        else:
            pass
            # print "No new messages."
        sleep(15)

except twilio.TwilioRestException as e:
    print e