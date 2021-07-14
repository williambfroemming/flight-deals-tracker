from twilio.rest import Client

AUTH_TOKEN = YOUR TWILIO AUTH TOKEN
ACCOUNT_SID = YOUR TWILIO ACCOUNT SID


class NotificationManager:

    def __init__(self):
        self.client = Client(ACCOUNT_SID, AUTH_TOKEN)

    def send_notification(self, message):
        message = self.client.messages.create(
            body=message,
            from_=YOUR TWILIO NUMBER,
            to=YOUR PHONE NUMBER
        )
        print(message.sid)
