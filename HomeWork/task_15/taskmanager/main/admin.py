from django.contrib import admin
from .models import Product


class ArticleAdmin(admin.ModelAdmin):
    fields = ('name', 'price', 'quantity', 'comment', 'user')
    search_fields = 'name',
    list_display = 'name', 'price', 'quantity', 'short_description', 'user',
    list_filter = 'user',


admin.site.register(Product, ArticleAdmin)
