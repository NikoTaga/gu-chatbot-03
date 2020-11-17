# Create your views here.
from django.shortcuts import render


def home(request):
    return render(request, 'ecom_chatbot/index.html')

def chat(request):
    return render(request, 'ecom_chatbot/chat.html')

def chats(request):
    return render(request, 'ecom_chatbot/chats.html')