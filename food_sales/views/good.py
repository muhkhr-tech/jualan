from django.shortcuts import render, redirect

from ..models import *

def index(request):
    data = Good.objects.all()

    context = {
        'data': data
    }

    return render(request, 'food_sales/good/index.html', context=context)

def create(request):
    if request.method == 'POST':
        new_good = Good()
        new_good.code = request.POST['good_code']
        new_good.name = request.POST['good_name']
        new_good.unit = request.POST['good_unit']
        new_good.save()

        return redirect('food_sales:good')
    
    return render(request, 'food_sales/good/create.html')
