from abc import ABCMeta, abstractmethod

from app.contexts.shared.notifications.domain.push_body_message import NotificationPushBodyMessage


class PushNotification(metaclass=ABCMeta):
    @abstractmethod
    def send(self, message: NotificationPushBodyMessage):
        """Load in the data set"""
        raise NotImplementedError