from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.contrib import messages

from restaurant.forms import OrderForm

from .models import *


class Home(generic.ListView):
    model = Food
    context_object_name = "foods"
    template_name = "index.html"


class Breakfast(Home):
    queryset = Food.objects.filter(food_type__title="صبحانه")


class Lunch(Home):
    queryset = Food.objects.filter(food_type__title="ناهار")


class Dinner(Home):
    queryset = Food.objects.filter(food_type__title="شام")


class FastFood(Home):
    queryset = Food.objects.filter(food_type__title="فست فود")


class Persian(Home):
    queryset = Food.objects.filter(food_type__title="ایرانی")


class Drinks(Home):
    queryset = Food.objects.filter(food_type__title="نوشیدنی")


class Detail(generic.DetailView):
    model = Food
    # context_object_name="food"
    template_name = "detail.html"

    # def post(self, request, *args, **kwargs):
    #     context = {"food": self.get_object()}
    #     return render(request, "order.html", context)


class AboutUs(generic.TemplateView):
    model = Food
    template_name = "about_us.html"


def contact_us(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        text = request.POST.get("description")
        SuggestionCritics.objects.create(name=name, email=email, text=text)
        context = {
            "name": name,
            "text": text,
        }
        return render(request, "conect_us_sent.html", context)
    return render(request, "conect_us.html")


class FoodOrder(generic.DetailView):
    model= Food
    template_name = "order.html"

    def post(self, request, pk, *args, **kwargs):
        # food= get_object_or_404(Food, pk=pk)
        order_form = OrderForm(request.POST)
        
        if order_form.is_valid():
            order_form.save()
        #     Order.objects.create(
        #         food=food,
        #         name=name,
        #         email=email,
        #         phone_number=phone_number,
        #         amount=amount,
        #     )
            context = {
                # "food": food,
                "name": order_form.cleaned_data.get("name"),
                "amount": order_form.cleaned_data.get("amount"),
                "phone_number": order_form.cleaned_data.get("phone_number"),
            }
            return render(request, "order_successful.html",context)
        messages.error(request,order_form.errors)
        context = {"food": self.get_object(), "form": order_form}
        return render(request, "order.html",context)
        
