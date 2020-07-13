from app.contexts.shared.notifications.domain.push_body_message import NotificationPushBodyMessage
from app.contexts.shared.notifications.infrastructure.push_notifications_fcm import PushNotificationsFcm


class NotifyHeroUsecase:
    def __init__(self):
        self.__notifier = PushNotificationsFcm()

    async def notify(self, token: str):
        return await self.__notifier.send(NotificationPushBodyMessage(
            title='New Hero',
            body='Firebase is awesome',
            icon='assets/icons/icon-48x48.png',
            token=token
        ))
