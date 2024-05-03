from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseRedirect, Http404, HttpResponseNotFound
from django.urls import reverse
from django.db import transaction
from django.contrib import messages

from datetime import datetime

from ..models import *

def index(request):
    data = Selling.objects.all()

    context = {
        'data': data
    }

    return render(request, 'food_sales/selling/index.html', context=context)

def create(request):
    if request.method == 'POST':
        new_selling = Selling()
        new_selling.code = request.POST['selling_code']
        new_selling.name = request.POST['selling_name']
        new_selling.date = datetime.now()
        new_selling.save()

        return HttpResponseRedirect(reverse("food_sales:selling.set_price", kwargs={"selling_id": new_selling.id}))
    
    return render(request, 'food_sales/selling/create.html')

def set_food_sale(request, selling_id):
    selling = get_object_or_404(Selling, pk=selling_id, status=False)
    foods = Food.objects.all()

    if request.method == 'POST':
        food = get_object_or_404(Food, pk=request.POST['food_id'])

        selling_food = SellingFood.objects.filter(selling=selling, food=food).first()

        if  not selling_food:
            new_selling_food = SellingFood()

            new_selling_food.selling = selling
            new_selling_food.food = food
            new_selling_food.unit = ''
            new_selling_food.amount = 0
            new_selling_food.total_price = 0
            new_selling_food.total_price_sale = 0

            new_selling_food.save()

            selling_food = new_selling_food

        return HttpResponseRedirect(reverse("food_sales:selling.set_price", kwargs={"selling_food_id": selling_food.id}))

    context = {
        'selling': selling,
        'foods': foods
    }

    return render(request, 'food_sales/selling/set-food-sale.html', context=context)

def set_price(request, selling_food_id):
    selling_food = get_object_or_404(SellingFood, pk=selling_food_id)
    
    ingredients = SellingFoodIngredient.objects.filter(selling_food=selling_food).all()

    context = {
        'selling_food': selling_food,
        'ingredienst': ingredients
    }

    return render(request, 'food_sales/selling/set-price.html', context=context)

def remove_ingredient(request, selling_id):
    if request.method == 'POST':

        food = get_object_or_404(Food, pk=selling_id, status=False)
        good = get_object_or_404(Good, pk=request.POST['good'])

        ingredient = Ingredient.objects.filter(
            food=food,
            good=good
        ).first()

        ingredient.delete()

        return HttpResponseRedirect(reverse("food_sales:selling.set_price", kwargs={"selling_id": selling_id}))
    
    return Http404()

def verify(request, selling_id):
    if request.method == 'POST':

        food = get_object_or_404(Food, pk=selling_id)

        ingredients = Ingredient.objects.filter(
            food=food
        ).all()

        if ingredients:
            for ingredient in ingredients:
                ingredient.good.stock -= ingredient.amount
                ingredient.good.save()
                    
            food.status = True
            food.save()
        else:
            messages.add_message(request, messages.WARNING, "Anda belum menambahkan bahan apapun kedalam makanan, silakan tambah bahan terlebih dahulu!")

        return redirect("food_sales:selling")
    
    return HttpResponseNotFound()

def detail(request, selling_id):
    food = get_object_or_404(Food, pk=selling_id)
    ingredients = Ingredient.objects.filter(
        food=food
    ).all()
    
    context = {
        'food': food,
        'ingredients': ingredients
    }

    return render(request, 'food_sales/selling/detail.html', context=context)