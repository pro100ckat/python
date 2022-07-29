from django.forms import ModelForm
from database.models import *


class Provider_Form(ModelForm):
    class Meta:

        fields = [ "provider_name", "provider_country", "provider_number", "provider_address"]
        labels = {
            "provider_name": "Наименование поставщика",
            "provider_country": "Страна поставщика",
            "provider_number": "Номер поставщика",
            "provider_address": "Адрес поставщика"
        }

class Firm_Form(ModelForm):
    class Meta:
        model = Firm
        fields = [ "firm_name", "firm_address", "firm_country", "firm_number", "firm_site"]
        labels = {
            "firm_name": "Наименование фирмы",
            "firm_country": "Страна фирмы",
            "firm_number": "Номер фирмы",
            "firm_address": "Адрес фирмы",
            "firm_site": "Сайт фирмы"
        }

class Seller_Form(ModelForm):
    class Meta:
        model = Seller
        fields = ["seller_name", "seller_exp", "seller_address"]
        labels = {
            "seller_name": "ФИО продавца",
            "seller_exp": "Опыт работы",
            "seller_address": "Адрес продавца",
        }

class Type_Form(ModelForm):
    class Meta:
        model = Equipment_type
        fields = ["et_name"]
        labels = {
            "et_name": "Наименование типа",
        }

class Equipment_Form(ModelForm):
    class Meta:
        model = Equipment
        fields = ["equipment_name", "equipment_price", "equipment_size", "equipment_date", "equipment_country", "id_equipment_type", "id_seller", "id_provider", "id_firm"]
        labels = {
            "equipment_name": "Оборудование",
            "equipment_price": "Цена",
            "equipment_size": "Количество",
            "equipment_date": "Дата поступления",
            "equipment_country": "Страна",
            "id_equipment_type": "Тип оборудования",
            "id_seller": "Продавец",
            "id_provider": "Поставщик",
            "id_firm": "Фирма производитель"
        }