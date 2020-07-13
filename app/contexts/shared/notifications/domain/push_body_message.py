class NotificationPushBodyMessage:
    def __init__(self, title: str, body: str, icon: str, token: str):
        self.token = token
        self.title = title
        self.body = body
        self.icon = icon

    def asdict(self):
        return {
            'title': self.title,
            'body': self.body,
            'icon': self.icon
        }
