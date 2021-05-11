from django.shortcuts import render
from mainapp.models import Product, ProductCategory


def main(request):
    products = Product.objects.all()[:4]

    context = {
        'slogan': "WOW КАКИЕ УДОБНЫЕ СТУЛЬЯ",
        'topic': 'Trends',
        'products': products,
    }
    return render(request, 'index.html', context=context)


def contact(request):
    return render(request, 'contact.html')
