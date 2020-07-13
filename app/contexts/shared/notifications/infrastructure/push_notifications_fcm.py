import httpx
import json
from http import HTTPStatus
import os
from app.contexts.shared.notifications.domain.push_body_message import NotificationPushBodyMessage
from app.contexts.shared.notifications.domain.push_notification import PushNotification
from app.contexts.shared.notifications.infrastructure.http_error_fcm import HttpErrorFCM


class PushNotificationsFcm(PushNotification):
    __url = 'https://fcm.googleapis.com/fcm/send'

    async def send(self, message: NotificationPushBodyMessage):
        async with self.__get_client() as client:
            try:
                data = {
                    'notification': {
                        'title': message.title,
                        'body': message.body,
                        'icon': message.icon
                    },
                    'to': message.token}
                response = await client.post(url=self.__url, data=json.dumps(data))
                response.raise_for_status()
                return response.json()
            except httpx.HTTPError as err:
                code = err.response.status_code
                if code == HTTPStatus.UNAUTHORIZED.value:
                    raise HttpErrorFCM(code, 'UNAUTHORIZED')
                if code == HTTPStatus.BAD_REQUEST.value:
                    raise HttpErrorFCM(code, 'BAD_REQUEST')
                raise HttpErrorFCM(code, 'ERROR_GENERAL')

    @staticmethod
    def __get_client():
        headers = {
            'Content-Type': 'application/json',
            'Authorization': f'key={os.environ.get("FCM_KEY_SERVER")}'
        }
        print('headers', headers)
        return httpx.AsyncClient(headers=headers)
