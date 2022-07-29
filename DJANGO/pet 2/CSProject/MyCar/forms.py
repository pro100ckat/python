from django import forms
from MyCar.models import *


class RentForm(forms.ModelForm):
    id_model = forms.ModelChoiceField(queryset=ModelCar.objects.all(), widget=forms.HiddenInput)
    class Meta:
        model = Rent
        fields = ['id_model','id_tariff','id_operator','name','phone','time']
        labels = {
            "id_model": "Модель",
            "id_tariff": "Выберите тариф",
            "id_operator": "Выберите оператора",
            "name": "Ваше имя",
            "phone": "Ваш телефон",
            "time": "Выберите количество часов аренды",
        }

class RankForM(forms.ModelForm):
    class Meta:
        model = Rank
        fields = ['name']
        labels = {
            'name': 'Название нового класса',
        }

class MarkForm(forms.ModelForm):
    class Meta:
        model = Mark
        fields = ['name',]
        labels = {
            'name': 'Название новой марки',
        }

class OperatorForm(forms.ModelForm):
    class Meta:
        model = Operator
        fields = ['name', 'photo', 'number']
        labels = {
            'name': 'Имя нового оператора',
            'photo': 'Фото нового оператора',
            'number': 'Номер телефона нового оператора',
        }

class TariffForm(forms.ModelForm):
    class Meta:
        model = Tariff
        fields = ['name','description','price']
        labels = {
            'name': 'Название нового тарифа',
            'description': 'Короткое описание нового тарифа',
            'price': 'Стоимость нового тарифа',
        }

class FuelForm(forms.ModelForm):
    class Meta:
        model = Fuel
        fields = ['name']
        labels = {
            'name': 'Название нового топлива',
        }

class ModelForm(forms.ModelForm):
    class Meta:
        model = ModelCar
        fields = ['name', 'mark_id', 'id_rank', 'id_fuel', 'photo']
        labels = {
            'name': 'Название новой модели',
            'id_fuel': 'Топливо новой модели',
            'id_rank': 'Название новой модели',
            'mark_id': 'Марка новой модели',
            'photo': 'Фото новой модели',

        }

class RentEditForm(forms.ModelForm):
    class Meta:
        model = Rent
        fields = ['id_model','id_tariff','id_operator','name','phone','time']
        labels = {
            "id_model": "Модель",
            "id_tariff": "Тариф",
            "id_operator": "Оператора",
            "name": "Имя арендателя",
            "phone": "Телефон арендателя",
            "time": "Количество часов аренды",
        }