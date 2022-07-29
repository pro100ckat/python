from django.forms import ModelForm
from avia.models import *


class Post_Form(ModelForm):
    class Meta:
        model = Post
        fields = ["post_name", "level"]
        labels = {
            "post_name": "Наименование должности",
            "level": "Уровень доступа",

        }

class Contacts_Form(ModelForm):
    class Meta:
        model = Contacts
        fields = ["phone_number", "mail", "address"]
        labels = {
            "phone_number": "Номер телефона",
            "mail": "Mail адресс",
            "address": "Адрес проживания",
        }

class Passenger_Form(ModelForm):
    class Meta:
        model = Passenger
        fields = ["code", "passport", "date", "first_name", "otchestvo", "lastname", "id_contacts"]
        labels = {
            "code": "Код пассажира",
            "passport": "Серия и номер паспорта",
            "date": "Дата рождения",
            "first_name": "Фамилия",
            "lastname": "Имя",
            "otchestvo": "Отчества",
            "id_contacts": "ID контактных данных",
        }

class Flight_conditions_Form(ModelForm):
    class Meta:
        model = Flight_conditions
        fields = ["flight_conditions_name", "vozvrat", "baggage", "animals"]
        labels = {
            "flight_conditions_name": "Код пассажира",
            "vozvrat": "Возврат билета",
            "baggage": "Масса багажа",
            "animals": "Животные",
        }

class Airports_Form(ModelForm):
    class Meta:
        model = Airports
        fields = ["airports_code", "airports_name", "airports_city", "timezone"]
        labels = {
            "airports_code": "Код аэропорта",
            "airports_name": "Название",
            "airports_city": "Город",
            "timezone": "Временная зона",
        }

class Company_Form(ModelForm):
    class Meta:
        model = Company
        fields = ["company_name", "address", "company_phone_number"]
        labels = {
            "company_name": "Название компании",
            "address": "Адресс",
            "company_phone_number": "Номер телефона",
        }

class Model_aircraft_Form(ModelForm):
    class Meta:
        model = Model_aircraft
        fields = ["model_aircraft_name", "kolvo_mest", "max_dal", "max_speed", "id_company"]
        labels = {
            "model_aircraft_name": "Название модели самолета",
            "kolvo_mest": "Количество мест",
            "max_speed": "Максимальная скорость",
            "max_dal": "Максимальная дальность",
         }

class Aircrafts_Form(ModelForm):
    class Meta:
        model = Aircrafts
        fields = ["model_aircraft_id"]
        labels = {
            "model_aircraft_id": "Код модели самолета",
         }

class Flights_Form(ModelForm):
    class Meta:
        model = Flight
        fields = ["flight_number", "vilet_time","prilet_time","flight_departure", "id_aircrafts", "flight_arrival"]
        labels = {
            "flight_number": "Номер рейса",
            "vilet_time": "Время вылета",
            "prilet_time": "Время прилета",
            "flight_departure": "Место вылета",
            "id_aircrafts": "ID самолета",
            "flight_arrival": "Место прилета",

             }

class Boarding_pass_Form(ModelForm):
    class Meta:
        model = Boarding_pass
        fields = ["boarding_pass_number", "mesto", "exit"]
        labels = {
            "boarding_pass_number": "Номер посадочного талона",
            "mesto": "Место",
            "exit": "Номер выхода на посадку",

         }

class Tickets_Form(ModelForm):
    class Meta:
        model = Tickets
        fields = ["tickets_number", "tickets_flight", "id_flight", "tickets_price", "status", "tickets_date", "id_boarding_pass", "id_flight_conditions", "id_passenger"]
        labels = {
            "tickets_number": "Номер билета",
            "tickets_flight": "Рейс",
            "id_flight" : "Рейс",
            "tickets_price": "Цена",
            "status": "Статус",
            "tickets_date": "Дата билета",
            "id_boarding_pass": "ID посадочного талона",
            "id_flight_conditions": "ID условий перелета",
            "id_passenger": "ID пассажира",
        }

class Staff_Form(ModelForm):
    class Meta:
        model = Staff
        fields = ["FIO", "grafik", "id_aircrafts","id_post"]
        labels = {
            "FIO": "ФИО",
            "grafik": "График работы",
            "id_aircrafts": "Номер самолета",
            "id_post": "Номер должности",
        }