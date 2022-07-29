from django.db import models

#Create your models here.

class Contacts(models.Model):
    contacts_id = models.AutoField(primary_key=models.ProtectedError)
    phone_number = models.CharField(max_length=50)
    mail = models.CharField(max_length=50)
    address = models.CharField(max_length=50)

    class Meta:
        verbose_name = "Контактные данные"
        verbose_name_plural = "Контактные данные"

    def __str__(self):
        return self.contacts_id

#Модель пассажир
class Passenger(models.Model):
    passenger_id = models.AutoField(primary_key=models.ProtectedError)
    code = models.IntegerField()
    passport = models.CharField(max_length=10)
    date = models.DateField()
    first_name = models.CharField(max_length=50)
    otchestvo = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    id_contacts = models.OneToOneField(Contacts, on_delete=models.PROTECT, default='',  related_name="contacts")

    class Meta:
        verbose_name = "Пассажир"
        verbose_name_plural = "Пассажиры"

    def __str__(self):
        return self.first_name


# Модель условия перелета
class Flight_conditions(models.Model):
    flight_conditions_id = models.AutoField(primary_key=models.ProtectedError)
    flight_conditions_name = models.CharField(max_length=30)
    vozvrat = models.CharField(max_length=10)
    baggage = models.IntegerField()
    animals = models.CharField(max_length=50)
    class Meta:
        verbose_name = "Условия перелета"
        verbose_name_plural = "Условие перелета"

    def __str__(self):
        return self.flight_conditions_name

#Модель аэроопрты
class Airports(models.Model):
    airports_id = models.AutoField(primary_key=models.ProtectedError)
    airports_code = models.IntegerField()
    airports_name = models.CharField(max_length=10)
    airports_city = models.CharField(max_length=20)
    timezone = models.CharField(max_length=3)
    class Meta:
        verbose_name = "Аэропорт"
        verbose_name_plural = "Аэропорты"

    def __str__(self):
        return self.airports_name

#Модель компании
class Company(models.Model):
    company_id = models.AutoField(primary_key=models.ProtectedError)
    company_name = models.CharField(max_length=30)
    address = models.CharField(max_length=50)
    company_phone_number = models.CharField(max_length=20)

    class Meta:
        verbose_name = "Производитель"
        verbose_name_plural = "Производители"

    def __str__(self):
        return self.company_name

#Модель самолета
class Model_aircraft(models.Model):
    model_aircraft_id= models.AutoField(primary_key=models.ProtectedError)
    model_aircraft_name = models.CharField(max_length=30)
    kolvo_mest = models.IntegerField()
    max_dal = models.IntegerField()
    max_speed = models.IntegerField()
    id_company = models.ForeignKey(Company, on_delete=models.CASCADE, default='')
    class Meta:
        verbose_name = "Модель самолета"
        verbose_name_plural = "Модель самолета"
    def __str__(self):
        return self.model_aircraft_name

#Самолеты
class Aircrafts(models.Model):
    aircrafts_id = models.AutoField(primary_key=models.ProtectedError)
    model_aircraft_id = models.ForeignKey(Model_aircraft, on_delete=models.CASCADE, default='')

    class Meta:
        verbose_name = "Самолет"
        verbose_name_plural = "Самолеты"

#Рейсы
class Flight(models.Model):
    flight_id = models.AutoField(primary_key=models.ProtectedError)
    flight_number = models.CharField(max_length=30)
    vilet_time = models.DateField()
    prilet_time = models.DateField()
    flight_departure = models.ForeignKey(Airports, on_delete=models.CASCADE, default='',  related_name="departure")
    flight_arrival = models.ForeignKey(Airports, on_delete=models.CASCADE, default='', related_name="arrival")
    id_aircrafts = models.OneToOneField(Aircrafts, on_delete=models.CASCADE, default='',  related_name="aircrafts")
    class Meta:
        verbose_name = "Рейсы"
        verbose_name_plural = "Рейсы"

    def __str__(self):
        return self.flight_number

# Модель Посадночный талон
class Boarding_pass(models.Model):
    boarding_pass_id = models.AutoField(primary_key=models.ProtectedError)
    boarding_pass_number = models.CharField(max_length=20)
    mesto = models.CharField(max_length=3)
    exit = models.CharField(max_length=1)

    class Meta:
        verbose_name = "Посадочный талон"
        verbose_name_plural = "Посадочные талоны"

    def __str__(self):
        return self.boarding_pass_number


#Модель билеты
class Tickets(models.Model):
    tickets_id = models.AutoField(primary_key=models.ProtectedError)
    tickets_number = models.IntegerField()
    tickets_flight = models.CharField(max_length=10)
    tickets_price = models.FloatField(default=0)
    status = models.CharField(max_length=50)
    tickets_date = models.DateField()
    id_flight = models.ForeignKey(Flight, on_delete=models.CASCADE, default='')
    id_boarding_pass = models.OneToOneField(Boarding_pass, on_delete=models.CASCADE, default='')
    id_flight_conditions = models.OneToOneField(Flight_conditions, on_delete=models.PROTECT)
    id_passenger = models.ForeignKey(Passenger, on_delete=models.CASCADE, default='')



    class Meta:
        verbose_name = "Билет"
        verbose_name_plural = "Билеты"
        #ordering =['tickets_number']

    def __str__(self):
        return self.flight

# Модель Должности
class Post(models.Model):
    post_id = models.AutoField(primary_key=models.ProtectedError)
    post_name = models.CharField(max_length=30)
    level = models.IntegerField()

    class Meta:
        verbose_name = "Дожность"
        verbose_name_plural = "Должности"

    def __str__(self):
        return self.post_name

#Персонал
class Staff(models.Model):
    staff_id = models.AutoField(primary_key=models.ProtectedError)
    grafik = models.CharField(max_length=10)
    FIO = models.CharField(max_length=60)
    id_aircrafts = models.ForeignKey(Aircrafts, on_delete=models.CASCADE, default='')
    id_post = models.ForeignKey(Post, on_delete=models.CASCADE, default='')

    class Meta:
        verbose_name = "Сотрудник"
        verbose_name_plural = "Сотрудники"
        # ordering =['tickets_number']

    def __str__(self):
        return self.FIO




