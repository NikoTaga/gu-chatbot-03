import json
from constants import BotType, ContentType, ChatType, MessageDirection, GenericTemplateActionType
from struct_dicts import *
from datetime import datetime
from pprint import pprint


def get_message(request) -> dict:
    '''
    утилита принимает запрос и преобразует его в словарь, который пришел от Jivo
    '''
    data = get_input_data(request.environ)
    if isinstance(data, bytes):
        json_message = data.decode('utf-8')
        message = json.loads(json_message)
        if isinstance(message, dict):
            return message


def get_input_data(env) -> bytes:
    content_length_data = env.get('CONTENT_LENGTH')
    content_length = int(content_length_data) if content_length_data else 0
    data = env['wsgi.input'].read(content_length) if content_length > 0 else b''
    return data


def procces_dict_received(message):

    import datetime
    # timestamp = 1339521878.04
    # value = datetime.datetime.fromtimestamp(timestamp)
    # print(value.strftime('%Y-%m-%d %H:%M:%S'))


    bot_id = 10
    message_id_in_messenger = message['id']
    chat_id_in_messenger = message['chat_id']
    content_type = ContentType.TEXT
    chat_type = ChatType.CHANNEL
    user_id_in_messenger = message['client_id']
    payload_text = message['message']['text']
    payload_direction = MessageDirection.RECEIVED
    ts_in_messenger = datetime.datetime.fromtimestamp(int(message['message']['timestamp']))

    payload = set_payload(direction=payload_direction,
                          text=payload_text)

    result = get_dict_received(bot_id=bot_id,
                               chat_id_in_messenger=chat_id_in_messenger,
                               content_type=content_type,
                               chat_type=chat_type,
                               user_id_in_messenger=user_id_in_messenger,
                               payload=payload,
                               message_id_in_messenger=message_id_in_messenger,
                               ts_in_messenger=ts_in_messenger,
                               )
    return result


def process_response_to_jiva(response):

    ts = str(datetime.today().timestamp())

    response_dict = {
        'event': 'BOT_MESSAGE',
        'id': 'hjghgjhg', #response['message_id_in_messenger'],
        'client_id': response['chat_id_in_messenger'],
        'message': {
            'timestamp': ts,
        },

    }

    if response['inline_buttons']:
        pass

    return response_dict







