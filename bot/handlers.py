from entities import EventCommandReceived, EventCommandToSend
from shop.models import Category, Product
from pprint import pprint
from constants import ContentType, ChatType, MessageDirection, GenericTemplateActionType
from struct_dicts import *


def message_handler(event: EventCommandReceived) -> EventCommandToSend:
    """Обработчик входящего сообщения"""

    # ПРИМЕР:

    direction = MessageDirection.SENT
    text = 'Сообщение клиенту Jiva'
    payload = set_payload(direction=direction, text=text)
    bot_id = event['bot_id']
    chat_id_in_messenger = event['user_id_in_messenger']
    inline_buttons = [
        {
            'text': "Да",
            'id': '1',
        }, {
            'text': "Нет",
            'id': '2'}]
    content_type = ContentType.MENU_BUTTON


    response = get_dict_response(bot_id=bot_id,
                               payload=payload,
                                inline_buttons=inline_buttons,
                               chat_id_in_messenger=chat_id_in_messenger,
                               content_type=content_type
                               )

    # преобразования полученного сообщения
    result = EventCommandToSend.Schema().dump(response)
    return result
