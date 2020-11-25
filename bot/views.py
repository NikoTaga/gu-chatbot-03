from django.http import HttpRequest
from django.shortcuts import render, HttpResponseRedirect

from clients.jivosite import JivositeClient
from clients.ok import OkClient
from entities import EventCommandReceived
from .handlers import message_handler


def ok_webhook(request: HttpRequest) -> None:
    client = OkClient()
    event = EventCommandReceived()
    result = message_handler(event)
    client.send_message(result)


def jivosite_webhook(request: HttpRequest) -> None:
    if request.method == 'POST':
        client = JivositeClient()
        # сообщение от JivaSite в формате словаря
        message = client.message_from_jiva(request.environ)
        print(message)

        # отправки тестового ответного сообщения на JivoSite
        client.send_message(None)

    # event = EventCommandReceived()
    # result = message_handler(event)
    # client.send_message(result)
    return render(request, 'ecom_chatbot/index.html')
