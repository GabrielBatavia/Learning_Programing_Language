from twilio.rest import Client
class NotificationManager:
    def __init__(self):
        self._account_sid = 'AC1cbce90ef10639154683628c3d7a049b'
        self._auth_token = '884aa622c4188be4aeaa596ca25ba50f'
        self.number = '+18289002723'
        self._client = Client(self._account_sid, self._auth_token)

    def send_msg(self, msg):
        message = self._client.messages.create(
            body=msg,
            from_=self.number,
            to=os.environ['ENV_NUMBER']
        )


if __name__ == '__main__':
    msg_sender = NotificationManager()
    msg_sender.send_msg("Hola")