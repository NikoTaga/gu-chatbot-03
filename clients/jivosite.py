from entities import EventCommandToSend
import json
import requests
from constants import URL_JIVOSITE


class JivositeClient:
    def __init__(self):
        pass


    def message_from_jiva(self, environ):
        data = self.get_input_data(environ)
        if isinstance(data, bytes):
            json_message = data.decode('utf-8')
            message = json.loads(json_message)
            if isinstance(message, dict):
                return message


    def get_input_data(self, env) -> bytes:
        content_length_data = env.get('CONTENT_LENGTH')
        # приводим к int
        content_length = int(content_length_data) if content_length_data else 0
        # считываем данные, если они есть
        data = env['wsgi.input'].read(content_length) if content_length > 0 else b''
        return data


    """Класс для работы с JivoSite"""

    def send_message(self, payload: EventCommandToSend):

        # тестовое сообщение
        response_to_jiva = {
            'event': "BOT_MESSAGE",
            'id': "123e4567-e89b-12d3-a456-426655440000",
            'client_id': "1234",
            'message': {
                'type': "BUTTONS",
                'title': "Вас интересует доставка в пределах МКАД?",
                'text': "Вас интересует доставка в пределах МКАД? Да / Нет",
                'timestamp': 1583910736,
                'buttons': [
                    {
                        'text': "Да",
                        'id': 1,
                    }, {
                        'text': "Нет",
                        'id': 2}]}}

        response = requests.post(URL_JIVOSITE, json=response_to_jiva)
        # проверка статуса отправки. Должен быть 200
        print(f'Статус отправки сообщения на JivoSite {response.status_code}')

        """Отпрвка сообщения"""
        pass
