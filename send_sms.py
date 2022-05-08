'''
:TODO
    - Remove hard coded number                  DONE
    - Remove the hard coded tokens -            DONE
'''
import os
from twilio.rest import Client


account_sid = os.environ.get('TWILIO_ACCOUNT_SID')
auth_token = os.environ.get('TWILIO_AUTH_TOKEN')
p_number = os.environ.get('P_PHONE_NUMBER')
t_number = os.environ.get('T_PHONE_NUMBER')
client = Client(account_sid, auth_token)


text_msg = open('workout_file.txt')
data = text_msg.read()
text_msg.close()

message = client.messages \
    .create(
         body=data,
         from_=t_number,
         to=p_number
     )

