from django.db import models
from twilio.rest import Client
import os
TWILIO_API_KEY = os.getenv("TWILIO_API_KEY")


class Message(models.Model):
    name = models.CharField(max_length=200)
    score = models.IntegerField(default=0)

    def __str__(self):
        return self.name

    def send_sms(self):
        """ Sends an SMS based on score """
        try:
            # Use your Twilio SID and Auth Token here (ensure these are correct)
            account_sid = 'ACc2c16042daed05d2f68e7c587edb3618'  # Twilio SID
            auth_token = 'ed71d88735ea35f50071aff65b97b670'   # Twilio Auth Token

            # Ensure SID and Auth Token are present
            if not account_sid or not auth_token:
                raise ValueError("Twilio SID or Auth Token not set.")

            client = Client(account_sid, auth_token)

            # Debug print statements to check account and token validity
            print(f"Twilio SID: {account_sid}")
            print(f"Twilio Auth Token: {auth_token}")

            # Send message based on score
            if self.score >= 70:
                message = client.messages.create(
                    body=f"Congratulations {self.name}, your score is {self.score}.",
                    from_='++17755516578',  # Your Twilio phone number
                    to='+639700918583'     # Recipient phone number
                )
                print(f"Message sent successfully! SID: {message.sid}")
            else:
                message = client.messages.create(
                    body=f"Sorry {self.name}, your score is {self.score}. Try again.",
                    from_='+17752629288',  # Your Twilio phone number
                    to='+639700918583'     # Recipient phone number
                )
                print(f"Message sent successfully! SID: {message.sid}")

        except Exception as e:
            # If there's an error, print the full exception message
            print(f"Error sending SMS: {e}")

    def save(self, *args, **kwargs):
        # Send SMS when saving the instance if the score is 70 or above
        self.send_sms()
        # Save the instance to the database
        return super().save(*args, **kwargs)
