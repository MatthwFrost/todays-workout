'''
:TODO
    - Remove the hard coded tokens -            DONE
'''
import os
from twilio.rest import Client


# Find your Account SID and Auth Token at twilio.com/console
# and set the environment variables. See http://twil.io/secure
account_sid = os.environ.get('TWILIO_ACCOUNT_SID')
auth_token = os.environ.get('TWILIO_AUTH_TOKEN')
client = Client(account_sid, auth_token)


text_msg = open('workout_file.txt')
data = text_msg.read()
text_msg.close()

message = client.messages \
    .create(
         body=data,
         from_='+19794065303',
         to='+4407568085248'
     )

print(message.sid)
