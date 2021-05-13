from django.shortcuts import render
from mainapp.models import ProductCategory, Product
from django.shortcuts import get_object_or_404


def products(request, pk=None):
    print(pk)
    title = 'продукты'

    categories = ProductCategory.objects.all()
    if pk is not None:
        if pk == 0:
            products = Product.objects.all().order_by('price')
            category = {'name': 'все'}
        else:
            category = get_object_or_404(ProductCategory, pk=pk)
            products = Product.objects.filter(category_id__pk=pk).order_by('price')

    context = {
        'title': title,
        'categories': categories,
        'category': category,
        'products': products,
    }

    return render(request, 'mainapp/products_list.html', context=context)
