import win32com.client
from twilio.rest import Client

outlook = win32com.client.Dispatch("outlook.Application")
outlook_ns = outlook.GetNamespace("MAPI")

myfolder = outlook_ns.Folders['aydin_halimi1@baylor.edu'].Folders['Inbox']

messages = myfolder.Items

messagecount = 0

for message in messages:
    if message.UnRead == True:
        print(message.sender)
        print(message.subject)

        if 'absence' in message.subject:
            print("Found message with absence")
            Msg = outlook.CreateItem(0)
            Msg.Importance = 1
            Msg.Subject = 'Got your ' + message.subject + 'email'
            Msg.HTMLBody = 'Hi' + str(message.sender) + "\n" + 'sorry you are not well'
            
            Msg.To = message.sender.getExchangeUser().PrimarySmtpAddress
            Msg.readReceiptRequested = True

            Msg.Send()

