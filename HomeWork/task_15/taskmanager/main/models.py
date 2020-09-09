from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse


class Product(models.Model):
    name = models.CharField('Название', max_length=50)
    price = models.IntegerField('Цена')
    quantity = models.IntegerField('Количество')
    comment = models.TextField('Комментарий')
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    """
    models.CASCADE - удаляет все
    models.SET_NULL() - ставит NULL
    models.SET_DEFAULT() - делает то что мы написали
    models.DO_NOTHING() - ничего не делает
    """

    def get_absolute_url(self):
        return reverse('product-details', args=[str(self.id)])

    @property
    def short_description(self):
        return self.comment[:10]

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"
