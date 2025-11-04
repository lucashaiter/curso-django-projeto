from django.shortcuts import render
from django.http import HttpResponse

# HTTP Request
def home_view(request):
    # return HTTP Response
    return render(request, 'recipes/home.html', context={
        'name': 'Lucas'
    })

def sobre_view(request):
    return render(request, 'temp/temp.html')

def contato_view(request):
    return HttpResponse('HTTP RESPONSE - CONTATO')
