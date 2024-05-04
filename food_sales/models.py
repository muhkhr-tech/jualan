from django.db import models

class Shopping(models.Model):
    code = models.CharField(max_length=5)
    name = models.CharField(max_length=50)
    date = models.DateField()
    status = models.BooleanField(default=False)

class Good(models.Model):
    code = models.CharField(max_length=5, unique=True)
    name = models.CharField(max_length=50)
    unit = models.CharField(max_length=10)
    stock = models.IntegerField(default=0)
    status = models.BooleanField(default=False)

class ShoppingGood(models.Model):
    shopping = models.ForeignKey(Shopping, on_delete=models.PROTECT)
    good = models.ForeignKey(Good, on_delete=models.PROTECT)
    unit = models.CharField(max_length=10)
    amount = models.IntegerField(default=0)
    price = models.BigIntegerField(default=0)

class Selling(models.Model):
    code = models.CharField(max_length=5)
    name = models.CharField(max_length=50)
    date = models.DateField()
    status = models.BooleanField(default=False)

class Food(models.Model):
    code = models.CharField(max_length=5)
    name = models.CharField(max_length=50)
    date = models.DateField()
    status = models.BooleanField(default=False)

class SellingFood(models.Model):
    selling = models.ForeignKey(Selling, on_delete=models.PROTECT)
    food = models.ForeignKey(Food, on_delete=models.PROTECT)
    unit = models.CharField(max_length=10)
    amount = models.IntegerField(default=0)
    # good_name = models.CharField(max_length=50)
    # good_price = models.BigIntegerField(default=0)
    # good_price_sale = models.BigIntegerField(default=0)
    total_price = models.BigIntegerField(default=0)
    total_price_sale = models.BigIntegerField(default=0)

class SellingFoodIngredient(models.Model):
    selling_food = models.ForeignKey(SellingFood, on_delete=models.PROTECT)
    good = models.ForeignKey(Good, on_delete=models.PROTECT)
    # unit = models.CharField(max_length=10)
    # amount = models.IntegerField(default=0)
    # good_name = models.CharField(max_length=50)
    price = models.BigIntegerField(default=0)
    price_sale = models.BigIntegerField(default=0)

class Ingredient(models.Model):
    food = models.ForeignKey(Food, on_delete=models.PROTECT)
    good = models.ForeignKey(Good, on_delete=models.PROTECT)
    unit = models.CharField(max_length=10)
    amount = models.IntegerField(default=0)

class MasterMaterial(models.Model):
    name = models.CharField(max_length=50)
    price = models.BigIntegerField(default=0)
    unit = models.CharField(max_length=10)
    amount = models.IntegerField(default=0)
    type = models.CharField(max_length=50)
    store_name = models.CharField(max_length=100)
    date = models.DateField()
    created_at = models.DateField()
    status = models.BooleanField(default=True)