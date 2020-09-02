from .models import Product
from django.forms import ModelForm, TextInput


class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'price', 'quantity', 'comment']
        widgets = {
            'name': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите название продукта',

            }),
            'price': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите цену продукта',
                'type': 'number'
            }),
            'quantity': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Количество',
                'type': 'number'
            }),
            'comment': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Комментарий',
            })
        }
