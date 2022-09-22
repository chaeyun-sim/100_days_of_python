from twilio.rest import Client

TWILIO_SID = 'AC3f9782873573fdc17b5afd00b5372f21'
TWILIO_NUM = "+19014459477"
TWILIO_AUTH_TOKEN = "bbe34d00bb9bc7b3e9c13f3e9dc143fc"


class NotificationManager:

    def __init__(self):
        self.client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)

    def send_sms(self, message):
        print("Ready to send.")
        message = self.client.messages.create(
            body=message,
            from_=TWILIO_NUM,
            to="+821036833426",
        )
        # Prints if successfully sent.
        print(message.sid)
        print("Sent!")
