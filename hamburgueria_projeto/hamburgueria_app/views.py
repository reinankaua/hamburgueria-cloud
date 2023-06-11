from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
import requests


def index(request):
    return render(request, 'index.html')


@csrf_exempt
def submit(request):
    if request.method == 'POST':
        hamburger = request.POST.get('hamburger', '')
        ingredients = request.POST.getlist('ingredients[]')

        send_to_telegram(hamburger, ingredients)

        return HttpResponse('Pedido enviado com sucesso!') 


def send_to_telegram(hamburger, ingredients):
    token = '6035941459:AAFQftHgAKqREqYUVeuxZqa9_pvumR1N3E4'
    chat_id = '5570584834'

    message = f'Pedido:\nHambúrguer: {hamburger}\nIngredientes adicionais: {", ".join(ingredients)}'

    url = f'https://api.telegram.org/bot{token}/sendMessage'
    data = {
        'chat_id': chat_id,               
        'text': message        
    }

    response = requests.post(url, data=data)

