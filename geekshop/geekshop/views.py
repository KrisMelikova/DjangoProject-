from django.shortcuts import render

from basketapp.models import Basket
from mainapp.models import Product, ProductCategory


def main(request):
    products = Product.objects.all()[:4]
    basket = ''
    if request.user.is_authenticated:
        basket = Basket.objects.filter(user=request.user)
    context = {
        'slogan': "WOW КАКИЕ УДОБНЫЕ СТУЛЬЯ",
        'topic': 'Trends',
        'products': products,
        'basket': basket,
    }
    return render(request, 'index.html', context=context)


def contact(request):
    return render(request, 'contact.html')
