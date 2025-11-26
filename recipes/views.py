from django.shortcuts import render
from utils.recipes.factory import make_recipe
from .models import Recipe, Category


def home(request):
    recipes = Recipe.objects.all().order_by('-id')
    return render(request, 'recipes/pages/home.html', context={
        'recipes': recipes
    })

def category(request, category_id):
    categories = Recipe.objects.filter(category__id = category_id).order_by('-id') 
    return render(request, 'recipes/pages/home.html', context={
        'categories': categories
    })

def recipe(request, id):    
    return render(request, 'recipes/pages/recipe-view.html', context={
        'recipe': make_recipe(),
        'is_detail_page': True
    })