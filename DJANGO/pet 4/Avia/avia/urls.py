from django.conf.urls import url, include
from avia import views

urlpatterns = [
    url(r"^main_menu/", views.main_menu, name="main_menu"),

    # URL post(Должности)
    url(r"^post/$", views.show_post, name="post"),
    url(r"^edit_post/(?P<id_post>\d+)$", views.edit_post, name="edit_post"),
    url(r"^delete_post/(?P<id_post>\d+)$", views.delete_post, name="delete_post"),
    url(r"^add_post$", views.add_post, name="add_post"),

    # URL aircrafts(Самолеты)
    url(r"^aircrafts/$", views.show_aircrafts, name="aircrafts"),
    url(r"^edit_aircrafts/(?P<id_aircrafts>\d+)$", views.edit_aircrafts, name="edit_aircrafts"),
    url(r"^delete_aircrafts/(?P<id_aircrafts>\d+)$", views.delete_aircrafts, name="delete_aircrafts"),
    url(r"^add_aircrafts$", views.add_aircrafts, name="add_aircrafts"),

    # URL staff(Сотрудники)
    url(r"^staff/$", views.show_staff, name="staff"),
    url(r"^edit_staff/(?P<id_staff>\d+)$", views.edit_staff, name="edit_staff"),
    url(r"^delete_staff/(?P<id_staff>\d+)$", views.delete_staff, name="delete_staff"),
    url(r"^add_staff$", views.add_staff, name="add_staff"),


    # URL flight(Рейсы)
    url(r"^flight/$", views.show_flight, name="flight"),
    url(r"^edit_flight/(?P<id_flight>\d+)$", views.edit_flight, name="edit_flight"),
    url(r"^delete_flight/(?P<id_flight>\d+)$", views.delete_flight, name="delete_flight"),
    url(r"^add_flight$", views.add_flight, name="add_flight"),

    # URL tickets(Билеты)

    url(r"^tickets/$", views.show_tickets, name="tickets"),
    url(r"^edit_tickets/(?P<id_tickets>\d+)$", views.edit_tickets, name="edit_tickets"),
    url(r"^delete_tickets/(?P<id_tickets>\d+)$", views.delete_tickets, name="delete_tickets"),
    url(r"^add_tickets$", views.add_tickets, name="add_tickets"),


    # URL model_aircraft(Модель самолета)

    url(r"^model_aircraft/$", views.show_model_aircraft, name="model_aircraft"),
    url(r"^edit_model_aircraft/(?P<id_model_aircraft>\d+)$", views.edit_model_aircraft, name="edit_model_aircraft"),
    url(r"^delete_model_aircraft/(?P<id_model_aircraft>\d+)$", views.delete_model_aircraft, name="delete_model_aircraft"),
    url(r"^add_model_aircraft$", views.add_model_aircraft, name="add_model_aircraft"),

    # URL company(Произовдитель)
    url(r"^company/$", views.show_company, name="company"),
    url(r"^edit_company/(?P<id_company>\d+)$", views.edit_company, name="edit_company"),
    url(r"^delete_company/(?P<id_company>\d+)$", views.delete_company, name="delete_company"),
    url(r"^add_company$", views.add_company, name="add_company"),

    # URL passenger(Пассажир)
    url(r"^passenger/$", views.show_passenger, name="passenger"),
    url(r"^edit_passenger/(?P<id_passenger>\d+)$", views.edit_passenger, name="edit_passenger"),
    url(r"^delete_passenger/(?P<id_passenger>\d+)$", views.delete_passenger, name="delete_passenger"),
    url(r"^add_passenger$", views.add_passenger, name="add_passenger"),

    # URL contacts(Контактные данные)
    url(r"^contacts/$", views.show_contacts, name="contacts"),
    url(r"^edit_contacts/(?P<id_contacts>\d+)$", views.edit_contacts, name="edit_contacts"),
    url(r"^delete_contacts/(?P<id_contacts>\d+)$", views.delete_contacts, name="delete_contacts"),
    url(r"^add_contacts$", views.add_contacts, name="add_contacts"),

    # URL flight_conditions(Условия перелета)
    url(r"^flight_conditions/$", views.show_flight_conditions, name="flight_conditions"),
    url(r"^edit_flight_conditions/(?P<id_flight_conditions>\d+)$", views.edit_flight_conditions, name="edit_flight_conditions"),
    url(r"^delete_flight_conditions/(?P<id_flight_conditions>\d+)$", views.delete_flight_conditions, name="delete_flight_conditions"),
    url(r"^add_flight_conditions$", views.add_flight_conditions, name="add_flight_conditions"),

    # URL airports(Аэропорты)
    url(r"^airports/$", views.show_airports, name="airports"),
    url(r"^edit_airports/(?P<id_airports>\d+)$", views.edit_airports, name="edit_airports"),
    url(r"^delete_airports/(?P<id_airports>\d+)$", views.delete_airports, name="delete_airports"),
    url(r"^add_airports$", views.add_airports, name="add_airports"),

    # URL boarding_pass(Посадочный талон)
    url(r"^boarding_pass/$", views.show_boarding_pass, name="boarding_pass"),
    url(r"^edit_boarding_pass/(?P<id_boarding_pass>\d+)$", views.edit_boarding_pass, name="edit_boarding_pass"),
    url(r"^delete_boarding_pass/(?P<id_boarding_pass>\d+)$", views.delete_boarding_pass, name="delete_boarding_pass"),
    url(r"^add_boarding_pass$", views.add_boarding_pass, name="add_boarding_pass"),

]


