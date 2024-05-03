from django.shortcuts import render

from ..models import *

def index(request):
    data = Good.objects.all()

    context = {
        'data': data
    }

    return render(request, 'food_sales/index.html', context=context)