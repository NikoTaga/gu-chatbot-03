from entities import EventCommandToSend
from bot.jivaservise import get_message, process_response_to_jiva, procces_dict_received
import json
import requests
from constants import URL_JIVOSITE
from pprint import pprint
import logging
import log.log_config


LOG = logging.getLogger('jivo')


class JivositeClient:
    """Класс для работы с JivoSite"""

    def receive_message(self, request):
        dict_from_ji = get_message(request)

        LOG.debug(f'from Jivo dict {dict_from_ji}')

        if dict_from_ji['event'] == 'CLIENT_MESSAGE':
            message = procces_dict_received(dict_from_ji)
            return message

    def send_message(self, payload: EventCommandToSend):
        """Отпрвка сообщения"""
        response_to_jiva = process_response_to_jiva(payload)
        response = requests.post(URL_JIVOSITE, json=response_to_jiva)

        LOG.debug(f'to Jivo cod {response.status_code} dict {response_to_jiva}')

        print(f'Статус отправки сообщения на JivoSite {response.status_code}')
