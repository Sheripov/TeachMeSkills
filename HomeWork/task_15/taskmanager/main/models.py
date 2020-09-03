from django.db import models


class Product(models.Model):
    name = models.CharField('Название', max_length=50)
    price = models.CharField('Цена', max_length=50)
    quantity = models.CharField('Количество', max_length=50)
    comment = models.CharField('Комментарий', max_length=50)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"


