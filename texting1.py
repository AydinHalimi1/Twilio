from twilio.rest import Client

accountSID = 'AC98e1847a66e3bb97170a435e3018d01f'

authToken = 'c924efa1f9b16fc3c5ea7460a05f29c6'

client = Client(accountSID,authToken)

TwilioNumber = "+12058902866"

mycellphone = "+17138165159"

textmessage = client.messages.create(to=mycellphone,from_=TwilioNumber,body="Hello World!")

print(textmessage.status)

#make a phone call

call = client.calls.create(url="http://demo.twilio.com/docs/voice.xml",to=mycellphone,from_=TwilioNumber)
