import datetime


def contact(phone_number: str = None,
                    first_name: str = None,
                    last_name: str = None,
                    user_id: int = None):
    contact_dict = {
        'phone_number': phone_number,
        'first_name': first_name,
        'last_name': last_name,
        'user_id': user_id,
    }
    return contact_dict


def set_generic_template_action(type: str,
                                link: str = None,
                                payload: str = None):
    # type - GenericTemplateActionType (POSTBACK) || (URL)
    generic_template_action_dict = {
        'type': type,
        'link': link,
        'payload': payload
    }
    return generic_template_action_dict


def set_inline_button(text: str,
                      action: dict):
    # fun set_generic_template_action -> action
    inline_button_dict = {
        'text': text,
        'action': action
    }
    return inline_button_dict


def set_generic_template(title: str,
                         description: str = None,
                         image_url: str = None,
                         action: dict = None,
                         buttons: list = None,
                         ):
    # buttons - [List[InlineButton]]
    generic_template_dict = {
        'title': title,
        'image_url': image_url,
        'description': description,
        'action': action,
        'buttons': buttons
    }
    return generic_template_dict


def set_payload(direction: int,
                text: str = None,
                contact: dict = None,
                image_url: str = None,
                file_url: str = None,
                video_url: str = None,
                inline: dict = None,
                command: str = None,
                voice: bytes = None,
                carousel: list = None
                ):
    # direction - MessageDirection (SEND) || (RECEIVED)
    payload_dict = {
        'direction': direction,
        'text': text,
        'contact': contact,
        'image_url': image_url,
        'file_url': file_url,
        'video_url': video_url,
        'inline': inline,
        'command': command,
        'voice': voice,
        'carousel': carousel
    }
    return payload_dict


def get_dict_response(bot_id: int,
                    chat_id_in_messenger: str,
                    content_type: int,
                    payload: dict,
                    message_id: int = None,
                    chat_id: int = None,
                    bot_user_id: int = None,
                    lang_code: str = None,
                    inline_buttons: list = None,
                    inline_buttons_cols: int = None,
                    ):
    '''
    утилита собирает словарь для EventCommandSend
    '''
    json_to_event = {
        'bot_id': bot_id,
        'chat_id_in_messenger': chat_id_in_messenger,
        'content_type': content_type,
        'payload': payload,
        'message_id': message_id,
        'chat_id': chat_id,
        'bot_user_id': bot_user_id,
        'lang_code': lang_code,
        'inline_buttons': inline_buttons,
        'inline_buttons_cols': inline_buttons_cols
    }
    return json_to_event


def get_dict_received(bot_id: int,
                    chat_id_in_messenger: str,
                    content_type: int,
                    payload: dict,
                    chat_type: int,
                    user_id_in_messenger: str,
                    bot_user_id: int = None,
                    message_id_in_messenger: str = None,
                    reply_id_in_messenger: str = None,
                    chat_avatar_in_messenger: str = None,
                    chat_name_in_messenger: str = None,
                    chat_url_in_messenger: str = None,
                    user_name_in_messenger: str = None,
                    user_url_in_messenger: str = None,
                    user_avatar_in_messenger: str = None,
                    ts_in_messenger: datetime = None,
                    ):
    '''
    утилита собирает словарь для EventCommandReceived
    '''
    dict = {
        'bot_id': bot_id,
        'chat_id_in_messenger': chat_id_in_messenger,
        'content_type': content_type,
        'payload': payload,
        'chat_type': chat_type,
        'user_id_in_messenger': user_id_in_messenger,
        'bot_user_id': bot_user_id,
        'message_id_in_messenger': message_id_in_messenger,
        'reply_id_in_messenger': reply_id_in_messenger,
        'chat_avatar_in_messenger': chat_avatar_in_messenger,
        'chat_name_in_messenger': chat_name_in_messenger,
        'chat_url_in_messenger': chat_url_in_messenger,
        'user_name_in_messenger': user_name_in_messenger,
        'user_url_in_messenger: ': user_url_in_messenger,
        'user_avatar_in_messenger: ': user_avatar_in_messenger,
        'ts_in_messenger': ts_in_messenger,
    }
    return  dict