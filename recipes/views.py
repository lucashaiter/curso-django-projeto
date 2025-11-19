from django.shortcuts import render

# HTTP Request
def home(request):
    # return HTTP Response
    return render(request, 'recipes/pages/home.html')

def recipe(request, id):
    return render(request, 'recipes/pages/recipe-view.html')