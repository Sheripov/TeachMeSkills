from django.shortcuts import render, redirect
from .models import Product
from .forms import ProductForm


def index(request):
    products = Product.objects.order_by('-id')
    return render(request, 'main/index.html', {'title': 'Главная страница сайта', 'products': products})


def add_product(request):
    error = ''
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
        else:
            error = 'Форма была неверной'

    form = ProductForm()
    context = {
        'form': form,
        'error': error
    }
    return render(request, 'main/add_product.html', context)