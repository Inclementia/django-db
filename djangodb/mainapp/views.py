from django.shortcuts import render

from mainapp.models import CategorySight


def city(request):
    return render(request, 'mainapp/city.html')


def categories(request):
    categories = CategorySight.objects.all()
    context = {
        'categories': categories,
        'page_title': 'Категории'
    }
    return render(request, 'mainapp/categories.html', context)


def index(request):
    return render(request, 'mainapp/index.html')


def catalog_page(request):
     pass

