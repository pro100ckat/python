from django.db import models

# Create your models here.

class Tariff(models.Model):
    tariff_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=300)
    price = models.IntegerField()

    class Meta():
        verbose_name = "Тариф"
        verbose_name_plural = "Тарифов"

    def __str__(self):
        return self.name


class Operator(models.Model):
    operator_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20)
    number = models.CharField(max_length=30)
    photo = models.ImageField()

    class Meta():
        verbose_name = "Оператор"
        verbose_name_plural = "Операторы"

    def __str__(self):
        return self.name

class Fuel(models.Model):
    fuel_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20)

    class Meta():
        verbose_name = "Топливо"
        verbose_name_plural = "Топлива"

    def __str__(self):
        return self.name


class Rank(models.Model):
    rank_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20)


    class Meta():
        verbose_name = "Класс"
        verbose_name_plural = "Классов"

    def __str__(self):
        return self.name

class Mark(models.Model):
    mark_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=60)


    class Meta():
        verbose_name = "Марка"
        verbose_name_plural = "Марок"

    def __str__(self):
        return self.name





class ModelCar(models.Model):
    model_car_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20)
    id_rank = models.ForeignKey(Rank, verbose_name="Класс")
    id_fuel = models.ForeignKey(Fuel, verbose_name="Топливо")
    mark_id = models.ForeignKey(Mark, verbose_name="Марка")
    photo = models.ImageField(blank=True, upload_to='MyCar/media')

    class Meta():
        verbose_name = "Модель"
        verbose_name_plural = "Модели"

    def __str__(self):
        return self.name


class Rent(models.Model):
    rent_id = models.AutoField(primary_key=True)
    id_tariff = models.ForeignKey(Tariff, verbose_name="Тариф")
    id_model = models.ForeignKey(ModelCar, verbose_name="Модель")
    id_operator = models.ForeignKey(Operator, verbose_name="Оператор")
    name = models.CharField(verbose_name='Арендатор', max_length=25, default='')
    phone = models.CharField(verbose_name='Телефон', max_length=11, default='')
    time = models.PositiveIntegerField()

    class Meta():
        verbose_name = "Аренда"
        verbose_name_plural = "Аренд"

    def __str__(self):
        return self.name




