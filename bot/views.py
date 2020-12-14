from django.http import HttpRequest
from django.shortcuts import render

from clients.jivosite import JivositeClient
from clients.ok import OkClient
from entities import EventCommandReceived
from .handlers import message_handler
from pprint import pprint


def ok_webhook(request: HttpRequest) -> None:
    client = OkClient()
    event = EventCommandReceived()
    result = message_handler(event)
    client.send_message(result)


def jivosite_webhook(request: HttpRequest) -> None:
    if request.method == 'POST':
        client = JivositeClient()
        message = client.receive_message(request)
        # pprint(message)
        event = EventCommandReceived.Schema().dump(message)
        # pprint('-------')
        # pprint(event)
        result = message_handler(event)
        # print('++++++++++')
        # pprint(result)
        client.send_message(result)
    return render(request, 'ecom_chatbot/index.html')
