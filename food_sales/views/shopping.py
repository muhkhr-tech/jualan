from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseRedirect, Http404, HttpResponseNotFound
from django.urls import reverse
from django.db import transaction
from django.contrib import messages

from datetime import datetime

from ..models import *

def index(request):
    data = Shopping.objects.all()

    context = {
        'data': data
    }

    return render(request, 'food_sales/shopping/index.html', context=context)

def create(request):
    if request.method == 'POST':
        new_shopping = Shopping()
        new_shopping.code = request.POST['shopping_code']
        new_shopping.name = request.POST['shopping_name']
        new_shopping.date = datetime.now()
        new_shopping.save()

        return HttpResponseRedirect(reverse("food_sales:shopping.add_good", kwargs={"shopping_id": new_shopping.id}))
    
    return render(request, 'food_sales/shopping/create.html')

def add_good(request, shopping_id):
    shopping = get_object_or_404(Shopping, pk=shopping_id, status=False)
    goods = Good.objects.all()
    shopping_goods = ShoppingGood.objects.filter(
        shopping=shopping
    )

    if request.method == 'POST':

        good = get_object_or_404(Good, pk=request.POST['good'])

        shopping_good = ShoppingGood.objects.filter(
            shopping=shopping,
            good=good
        ).first()

        if shopping_good:
            shopping_good.amount = request.POST['good_amount']
            shopping_good.price = request.POST['good_price']
            shopping_good.save()
        else:
            new_shopping_good = ShoppingGood()
            new_shopping_good.shopping = shopping
            new_shopping_good.good = good
            new_shopping_good.unit = good.unit
            new_shopping_good.amount = request.POST['good_amount']
            new_shopping_good.price = request.POST['good_price']
            new_shopping_good.save()

        return HttpResponseRedirect(reverse("food_sales:shopping.add_good", kwargs={"shopping_id": shopping_id}))
    
    context = {
        'shopping': shopping,
        'goods': goods,
        'shopping_goods': shopping_goods
    }

    return render(request, 'food_sales/shopping/add-good.html', context=context)

def remove_good(request, shopping_id):
    if request.method == 'POST':

        shopping = get_object_or_404(Shopping, pk=shopping_id, status=False)
        good = get_object_or_404(Good, pk=request.POST['good'])

        shopping_good = ShoppingGood.objects.filter(
            shopping=shopping,
            good=good
        ).first()

        shopping_good.delete()

        return HttpResponseRedirect(reverse("food_sales:shopping.add_good", kwargs={"shopping_id": shopping_id}))
    
    return Http404()

def verify(request, shopping_id):
    if request.method == 'POST':

        shopping = get_object_or_404(Shopping, pk=shopping_id)

        shopping_goods = ShoppingGood.objects.filter(
            shopping=shopping
        ).all()

        if shopping_goods:
            for shopping_good in shopping_goods:
                shopping_good.good.stock += shopping_good.amount
                shopping_good.good.save()
                    
            shopping.status = True
            shopping.save()
        else:
            messages.add_message(request, messages.WARNING, "Anda belum menambahkan barang apapun kedalam belanjaan, silakan tambah barang terlebih dahulu!")

        return redirect("food_sales:shopping")
    
    return HttpResponseNotFound()

def detail(request, shopping_id):
    shopping = get_object_or_404(Shopping, pk=shopping_id)
    shopping_goods = ShoppingGood.objects.filter(
        shopping=shopping
    )
    
    context = {
        'shopping': shopping,
        'shopping_goods': shopping_goods
    }

    return render(request, 'food_sales/shopping/detail.html', context=context)