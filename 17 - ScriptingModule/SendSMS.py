# Your Account Sid and Auth Token from twilio.com/console
# DANGER! This is insecure. See http://twil.io/secure
from twilio.rest import Client 
 
account_sid = '[account_sid]' 
auth_token = '[AuthToken]' 
client = Client(account_sid, auth_token) 
 
message = client.messages.create( 
                              from_='[twilio_number]',  
                              body='[Insert_Message_Here]',      
                              to='[number_to_SMS]' 
                          ) 
 
print(message.sid)