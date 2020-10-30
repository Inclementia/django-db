from django.shortcuts import render

from mainapp.models import CategorySight, Sight


def city(request):
    return render(request, 'mainapp/city.html')


def categories(request):
    categories = CategorySight.objects.all()
    context = {
        'categories': categories,
        'page_title': 'категории'
    }
    return render(request, 'mainapp/categories.html', context)


def index(request):
    return render(request, 'mainapp/index.html')


def sight_page(request, pk):
    sightes = Sight.objects.filter(category_id=pk)
    context = {
        'sightes': sightes,
        'page_title': 'страница категории'
    }
    return render(request, 'mainapp/sight_page.html', context)