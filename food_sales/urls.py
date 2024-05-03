from django.urls import path

from . import views
from .views import good as good_views
from .views import shopping as shopping_views
from .views import food as food_views
from .views import selling as selling_views
from .views import master as master_views

app_name='food_sales'

urlpatterns = [
    path('food-sales/', views.index, name='index'),
    path('food-sales/good/', good_views.index, name='good'),
    path('food-sales/good/create', good_views.create, name='good.create'),

    path('food-sales/shopping/', shopping_views.index, name='shopping'),
    path('food-sales/shopping/create', shopping_views.create, name='shopping.create'),
    path('food-sales/shopping/<int:shopping_id>/add-good', shopping_views.add_good, name='shopping.add_good'),
    path('food-sales/shopping/<int:shopping_id>/remove-good', shopping_views.remove_good, name='shopping.remove_good'),
    path('food-sales/shopping/<int:shopping_id>/verify', shopping_views.verify, name='shopping.verify'),
    path('food-sales/shopping/<int:shopping_id>/detail', shopping_views.detail, name='shopping.detail'),

    path('food-sales/food/', food_views.index, name='food'),
    path('food-sales/food/create', food_views.create, name='food.create'),
    path('food-sales/food/<int:food_id>/add-ingredient', food_views.add_ingredient, name='food.add_ingredient'),
    path('food-sales/food/<int:food_id>/remove-ingredient', food_views.remove_ingredient, name='food.remove_ingredient'),
    path('food-sales/food/<int:food_id>/verify', food_views.verify, name='food.verify'),
    path('food-sales/food/<int:food_id>/detail', food_views.detail, name='food.detail'),

    path('food-sales/selling/', selling_views.index, name='selling'),
    path('food-sales/selling/create', selling_views.create, name='selling.create'),
    path('food-sales/selling/<int:selling_id>/set-food-sale', selling_views.set_food_sale, name='selling.set_food_sale'),
    path('food-sales/selling/<int:selling_food_id>/set-price', selling_views.set_price, name='selling.set_price'),
    path('food-sales/selling/<int:selling_id>/remove-ingredient', selling_views.remove_ingredient, name='selling.remove_ingredient'),
    path('food-sales/selling/<int:selling_id>/verify', selling_views.verify, name='selling.verify'),
    path('food-sales/selling/<int:selling_id>/detail', selling_views.detail, name='selling.detail'),

    path('food-sales/master/materials', master_views.get_materials, name='master.material'),
    path('food-sales/master/material/insert', master_views.insert_materials, name='master.material.insert'),
]