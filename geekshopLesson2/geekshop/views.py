from django.shortcuts import render


def main(request):
    context = {
        'slogan': "WOW КАКИЕ УДОБНЫЕ СТУЛЬЯ",
        'topic': 'Trends'
    }
    return render(request, 'index.html', context=context)


def contact(request):
    return render(request, 'contact.html')
