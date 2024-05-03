from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseRedirect, Http404, HttpResponseNotFound
from django.urls import reverse
from django.db import transaction
from django.contrib import messages

from datetime import datetime

from ..models import *

def index(request):
    data = Food.objects.all()

    context = {
        'data': data
    }

    return render(request, 'food_sales/food/index.html', context=context)

def create(request):
    if request.method == 'POST':
        new_food = Food()
        new_food.code = request.POST['food_code']
        new_food.name = request.POST['food_name']
        new_food.date = datetime.now()
        new_food.save()

        return HttpResponseRedirect(reverse("food_sales:food.add_ingredient", kwargs={"food_id": new_food.id}))
    
    return render(request, 'food_sales/food/create.html')

def add_ingredient(request, food_id):
    food = get_object_or_404(Food, pk=food_id, status=False)
    goods = Good.objects.all()
    ingredients = Ingredient.objects.filter(
        food=food
    )

    if request.method == 'POST':

        good = get_object_or_404(Good, pk=request.POST['good'])

        ingredient = Ingredient.objects.filter(
            food=food,
            good=good
        ).first()

        if ingredient:
            ingredient.amount = request.POST['ingredient_amount']
            ingredient.save()
        else:
            new_ingredient = Ingredient()
            new_ingredient.food = food
            new_ingredient.good = good
            new_ingredient.unit = good.unit
            new_ingredient.amount = request.POST['ingredient_amount']
            new_ingredient.save()

        return HttpResponseRedirect(reverse("food_sales:food.add_ingredient", kwargs={"food_id": food_id}))
    
    context = {
        'food': food,
        'goods': goods,
        'ingredients': ingredients
    }

    return render(request, 'food_sales/food/add-ingredient.html', context=context)

def remove_ingredient(request, food_id):
    if request.method == 'POST':

        food = get_object_or_404(Food, pk=food_id, status=False)
        good = get_object_or_404(Good, pk=request.POST['good'])

        ingredient = Ingredient.objects.filter(
            food=food,
            good=good
        ).first()

        ingredient.delete()

        return HttpResponseRedirect(reverse("food_sales:food.add_ingredient", kwargs={"food_id": food_id}))
    
    return Http404()

def verify(request, food_id):
    if request.method == 'POST':

        food = get_object_or_404(Food, pk=food_id)

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

        return redirect("food_sales:food")
    
    return HttpResponseNotFound()

def detail(request, food_id):
    food = get_object_or_404(Food, pk=food_id)
    ingredients = Ingredient.objects.filter(
        food=food
    ).all()
    
    context = {
        'food': food,
        'ingredients': ingredients
    }

    return render(request, 'food_sales/food/detail.html', context=context)