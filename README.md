# GeekBrains Chat Bot Service

1. Entities (датаклассы)
    - EventCommandReceived
    - EventCommandToSend
    - клик на инлайн-кнопку
    - команда
2. Интерфейс адаптеров
3. Движок чат-бота и ИМ
    - модели каталога
        - Category
        - Product
        - Order
    - модели
        - BotUser
        - Chat
        - Message
    - код, который решает, что отправить
4. Константы из файла constants (нужные для моделей)
5. Интерфейс платежного модуля
    - модели
        - Банковская карта
        - Платеж (Payment)
    - интерфейс функций


## Разворачивание проекта
1.  Клонируем репозиторий
    git clone https://github.com/manchenkoff/gu-chatbot-03
2.  Устанавливаем виртуальное окружение
    sudo pip install virtualenv
    Создаем окружение в папке проекта
    virtualenv venv
    Активируем его:

        source venv/bin/activate (для oc unix)

        \Путь до папки проекта\project\venv\Scripts\activate.bat (для oc windows)

3.  Устанавливаем зависимости
    pip install -r requirements.txt
4.  Выполняем миграции
    python manage.py makemigrations
    python manage.py migrate    


##  Cоздание начального пользователя для авторизации в django-admin
1.  Выполняем миграции
    python manage.py makemigrations
    python manage.py migrate 
2.  Создаем суперюзера 
    python manage.py createsuperuser
3.  Запускаем сервер 
    python manage.py runserver    
4.  Проверка юзера
    http://127.0.0.1:8000/admin/


## Задача

Сделать простейший чат-бот для продажи и оплаты товаров в Одноклассниках и чате на сайте.

**Пример диалога с ботом:**

```
- Здравствуйте
- Здравствуйте, Евгений! Выберите категорию товаров: ...
- <кликнул на кнопку>
- Выберите товар: ...
- <кликнул на кнопку>
- Оплатите товар по ссылке: ...
- <произвел оплату>
- Спасибо! Начать заново?
```

Задача делится на 3 группы работ:

### 1. Подключить каналы:

1. [JivoSite](docs/jivosite.md)
2. [Одноклассники](docs/ok.md)

### 2. Подключить платежные системы:

1. [Stripe](https://stripe.com/)
2. [PayPal](https://www.paypal.com/ru/home)
3. [Click.uz](http://click.uz/)
4. [Paymo.uz](https://paymo.uz/)

### 3. Реализовать бизнес-логику:

1. [Разработать простейший интерфейс для просмотра диалогов](docs/chat_interface.md)
2. Разрботать обработчики сообщений пользователя

## Архитектура

Чат-бот состоит из четырех частей:

1. Адаптеры к каналам
    - `EventCommandReceived`
    - `EventCommandToSend`
    - клик на инлайн-кнопку
    - команда
2. Движок магазина
3. Модуль платежных систем
4. Интерфейс чатов

**Как все работает:**

- Сообщения, поступающие в любой канал, преобразуются адаптером в универсальный формат `EventCommandReceived`
- Движок магазина обрабатывает входящее сообщение и выдает ответ универсальном формате `EventCommandToSend`
- Адаптер конкретного канала преобразует исходящее сообщение в запрос к АПИ ботов.

## Настройка виртуального окружения:
- если не установлен пакет python3-venv, естанавливаем его:
    sudo apt-get install python3-venv

- создаем виртуальное окружение
    python3 -m venv ../venv_chb

- запускаем виртуальное окружение
    source ../venv_chb/bin/activate

- деактивация виртуального окружения
    deactivate 
    
## Установка зависимостей
    pip install -r requirements.txt

## Перед отправкой кода проверь:

```bash
mypy ./
flake8 ./
```
