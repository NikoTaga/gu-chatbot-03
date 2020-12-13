import os
import logging

LOG_FILE = 'jivosite.log'
LOG_DIR = 'logs'

PATH = os.path.dirname(os.path.abspath(__file__))
PATH = os.path.join(PATH, LOG_DIR, LOG_FILE)

# формировщик логов
FORMATTER = logging.Formatter(
    '%(asctime)s %(levelname) -8s %(module)s %(message)s')

# обработчики
STREAM_HANDLER = logging.StreamHandler()
STREAM_HANDLER.setFormatter(FORMATTER)
STREAM_HANDLER.setLevel(logging.ERROR)

FILE_HANDLER = logging.FileHandler(PATH, encoding='utf-8')
FILE_HANDLER.setFormatter(FORMATTER)
FILE_HANDLER.setLevel(logging.DEBUG)

# регистратор
LOGGER = logging.getLogger('jivo')
LOGGER.addHandler(FILE_HANDLER)
LOGGER.addHandler(STREAM_HANDLER)
LOGGER.setLevel(logging.DEBUG)

# тест
if __name__ == '__main__':
    LOGGER.critical('тест. критическое сообщение')
    LOGGER.error('тест. сообщение об ошибке')
    LOGGER.info('тест. информационное сообщение')
    LOGGER.debug('тест. отладочная информация')