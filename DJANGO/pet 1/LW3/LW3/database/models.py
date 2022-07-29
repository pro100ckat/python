from django.db import models

# Create your models here.

class Provider(models.Model):
    provider_id = models.AutoField(primary_key=True)
    provider_name = models.CharField(max_length=50)
    provider_address = models.CharField(max_length=50)
    provider_country = models.CharField(max_length=30)
    provider_number = models.CharField(max_length=50)
    class Meta:
        verbose_name = "Поставщик"
        verbose_name_plural = "Поставщики"

    def __str__(self):
        return self.provider_name

class Firm(models.Model):
    firm_id = models.AutoField(primary_key=True)
    firm_name = models.CharField(max_length=50)
    firm_address = models.CharField(max_length=50)
    firm_country = models.CharField(max_length=30)
    firm_number = models.CharField(max_length=50)
    firm_site = models.CharField(max_length=50)
    class Meta:
        verbose_name = "Фирма"
        verbose_name_plural = "Фирмы"



    def __str__(self):
        return self.firm_name

class Seller(models.Model):
    seller_id = models.AutoField(primary_key=True)
    seller_name = models.CharField(max_length=50)
    seller_address = models.CharField(max_length=50)
    seller_exp = models.IntegerField()
    provider_number = models.CharField(max_length=50)

    class Meta:
        verbose_name = "Продавец"
        verbose_name_plural = "Продавцы"


    def __str__(self):
        return self.seller_name

class Equipment_type(models.Model):
    et_id = models.AutoField(primary_key=True)
    et_name = models.CharField(max_length=50)
    def __str__(self):
        return self.et_name
    class Meta:
        verbose_name = "Тип оборудования"
        verbose_name_plural = "Типы оборудований"



class Equpment_type_seller(models.Model):
    et_id_f = models.ForeignKey(Equipment_type, models.ProtectedError)
    sel_id = models.ForeignKey(Seller, models.ProtectedError)

class Equipment(models.Model):
    equipment_id = models.AutoField(primary_key=models.ProtectedError)
    equipment_name = models.CharField(max_length=50)
    equipment_price = models.IntegerField()
    equipment_size = models.IntegerField(default=0)
    equipment_date = models.DateField()
    equipment_country = models.CharField(max_length=50)
    id_firm = models.ForeignKey(Firm, on_delete=models.CASCADE)
    id_provider = models.ForeignKey(Provider, on_delete=models.CASCADE)
    id_equipment_type = models.ForeignKey(Equipment_type, on_delete=models.CASCADE)
    id_seller = models.ForeignKey(Seller, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Оборудование"
        verbose_name_plural = "Оборудование"


    def __str__(self):
        return self.equipment_name

