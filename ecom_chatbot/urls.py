"""ecom_chatbot URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
import ecom_chatbot.views as ecom_chatbot

from bot.views import jivosite_webhook, ok_webhook

urlpatterns = [
    path('', ecom_chatbot.home, name='home'),
    path('chat/', ecom_chatbot.chat, name='chat'),
    path('chats/', ecom_chatbot.chats, name='chats'),
    path('admin/', admin.site.urls),
    # path('ok_webhook/', ok_webhook),
    path('jivosite_webhook/gu-chatbot-03', jivosite_webhook),
]
