from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from .models import Product
from django.views.generic.edit import CreateView, UpdateView, DeleteView


class ProductCreate(PermissionRequiredMixin, CreateView):
    permission_required = 'polls.can_add'
    model = Product
    fields = ['name', 'price', 'quantity', 'comment']


class ProductUpdate(PermissionRequiredMixin, UpdateView):
    permission_required = 'polls.can_edit'
    model = Product
    fields = ['name', 'price', 'quantity', 'comment']


class ProductDelete(PermissionRequiredMixin, DeleteView):
    permission_required = 'polls.can_delete'
    model = Product
    success_url = reverse_lazy('index')


def product_detail(request, id: int):
    products = Product.objects.filter(id=id)
    return render(request, 'main/index.html', {'title': 'Главная страница сайта', 'products': products})


def index(request):
    products = Product.objects.order_by('-id')
    return render(request, 'main/index.html', {'title': 'Главная страница сайта', 'products': products})
