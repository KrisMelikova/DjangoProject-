from django.shortcuts import render


def products(request):
    links_menu = {'links': [
        {'href': 'index', 'name': 'все'},
        {'href': 'index', 'name': 'дом'},
        {'href': 'index', 'name': 'офис'},
        {'href': 'index', 'name': 'модерн'},
        {'href': 'index', 'name': 'классика'},
    ]}
    return render(request, 'mainapp/products.html', context=links_menu)
