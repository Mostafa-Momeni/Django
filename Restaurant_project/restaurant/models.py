from django.db import models
from django.core.validators import MaxLengthValidator,MinLengthValidator,MaxValueValidator,MinValueValidator
from django.shortcuts import reverse

class FoodType(models.Model):
    title = models.CharField(max_length=255)
    
    def __str__(self):
        return f"{self.title}"
    

class Food(models.Model):
    name = models.CharField(max_length=255)
    ingredients = models.CharField(max_length=255,blank=True)
    weight = models.PositiveIntegerField(null=True,blank=True)
    length = models.PositiveIntegerField(null=True,blank=True)
    description = models.TextField(blank=True)
    old_price = models.PositiveIntegerField(null=True,blank=True)
    price = models.PositiveIntegerField()
    image = models.ImageField(upload_to="foods/")
    food_type = models.ManyToManyField(to=FoodType)
    
    def get_absolute_url(self):
        return reverse("detail", kwargs={"pk": self.pk})
    
    def __str__(self):
        return f"{self.name}"
    
    
    
class SuggestionCritics(models.Model):
    name = models.CharField(max_length=255,blank=True)
    email = models.EmailField(blank=True)
    text = models.TextField()
    

class Order(models.Model):
    food = models.ForeignKey(to=Food,on_delete=models.CASCADE,null=True)
    name = models.CharField(max_length=255)
    email = models.EmailField(blank=True)
    phone_number = models.CharField(max_length=255,validators=[MinLengthValidator(11, "طول شماره موبایل حتما باید 11 رقم باشد"),MaxLengthValidator(11, "طول شماره موبایل حتما باید 11 رقم باشد")])
    amount = models.PositiveIntegerField(validators=[MinValueValidator(1, "حداقل سفارش 1 عدد می باشد"), MaxValueValidator(10,"حداکثر سفارش 10 عدد می باشد")])