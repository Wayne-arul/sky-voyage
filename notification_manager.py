from twilio.rest import Client

TWILIO_SID = "AC7ba31dbf41eb1eaf17488cce36934a6y"
TWILIO_AUTH_TOKEN = "0c5736516be33ebbe96734fd8e054622"

class NotificationManager:

    def __init__(self):
        self.client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)

    def send_sms(self, message):
        message = self.client.messages.create(
            body=message,
            from_='+19704745691',
            to='+917201234465'
        )

        print(message.sid)