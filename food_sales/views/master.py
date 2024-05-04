from django.shortcuts import render, redirect

from datetime import datetime

from ..models import *

def get_materials(request):
    data = MasterMaterial.objects.all()

    context = {
        'data': data
    }

    return render(request, 'food_sales/master/material.html', context=context)

def insert_materials(request):
    if request.method == 'POST':
        new_good = MasterMaterial()
        new_good.price = request.POST['good_price']
        new_good.name = request.POST['good_name']
        new_good.unit = request.POST['good_unit']
        new_good.amount = request.POST['good_amount']
        new_good.type = request.POST['good_type']
        new_good.store_name = request.POST['good_store_name']
        new_good.date = request.POST['good_shop_date']
        new_good.created_at = datetime.now()
        new_good.save()

        return redirect('food_sales:master.material')
    
    return render(request, 'food_sales/master/material-insert.html')