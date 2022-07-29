from django.db import models
from django.contrib.auth.models import User

class PizzaShop(models.Model):
    name = models.CharField(max_length=30, verbose_name='Пицерия')
    description = models.TextField(verbose_name='Описание')
    rating = models.FloatField(default=0, verbose_name='Рейтинг')
    urls = models.URLField(verbose_name='Интернет адресс')

    def __str__(self):
        return self.name
    class Meta:
        verbose_name = 'Пиццерия'
        verbose_name.plural = 'Пицерии'

class Pizza(models.Model):
    pizzashop = models.ForeignKey(PizzaShop)
    name = models.CharField(max_length=30)
    short_description = models.CharField(max_length=100)
    image = models.ImageField(upload_to='pizza_images/', blank=False)
    price = models.IntegerField(default=0)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Пицца'
        verbose_name_plural = 'Пиццы'
        ordering = ['name']
