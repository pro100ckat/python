from django.shortcuts import render, redirect
from avia.forms import *
from avia.models import *

# Create your views here.
def main_menu(request):
    return render(request, "main.html", locals())

#SHOW FUCCTIONS
def show_post(request):
    post_list = Post.objects.all()
    return render(request, "post/show_post.html", locals())
def add_post(request):
    form = Post_Form()
    if request.method == "POST":
        form = Post_Form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('post')
        else:
            return render(request, "post/add_post.html", locals())
    return render(request, "post/add_post.html", locals())
def edit_post(request, id_post):
    post = Post.objects.get(post_id=id_post)
    form = Post_Form(instance=post)
    if request.method == "POST":
        form = Post_Form(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('post')
        else:
            return render(request, 'post/edit_post.html', locals())
    return render(request, 'post/edit_post.html', locals())
def delete_post(request, id_post):
    post = Post.objects.get(post_id=id_post)
    if request.method == "POST":
        if 'yes' in request.POST.keys() and request.POST['yes']:
            post.delete()
            return redirect('post')
        else:
            return redirect("post")
    return render(request, "post/delete_post.html", locals())


def show_contacts(request):
    contacts_list = Contacts.objects.all()
    return render(request, "contacts/show_contacts.html", locals())
def add_contacts(request):
    form = Contacts_Form()
    if request.method == "POST":
        form = Contacts_Form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('contacts')
        else:
            return render(request, "contacts/add_contacts.html", locals())
    return render(request, "contacts/add_contacts.html", locals())
def delete_contacts(request, id_contacts):
    contacts = Contacts.objects.get(contacts_id=id_contacts)
    if request.method == "POST":
        if 'yes' in request.POST.keys() and request.POST['yes']:
            contacts.delete()
            return redirect('contacts')
        else:
            return redirect("contacts")
    return render(request, "contacts/delete_contacts.html", locals())
def edit_contacts(request, id_contacts):
    contacts = Contacts.objects.get(contacts_id=id_contacts)
    form = Contacts_Form(instance=contacts)
    if request.method == "POST":
        form = Contacts_Form(request.POST, instance=contacts)
        if form.is_valid():
            form.save()
            return redirect('contacts')
        else:
            return render(request, 'contacts/edit_contacts.html', locals())
    return render(request, 'contacts/edit_contacts.html', locals())



def show_passenger(request):
    passenger_list = Passenger.objects.all()
    return render(request, "passenger/show_passenger.html", locals())
def add_passenger(request):
    form = Passenger_Form()
    if request.method == "POST":
        form = Passenger_Form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('passenger')
        else:
            return render(request, "passenger/add_passenger.html", locals())
    return render(request, "passenger/add_passenger.html", locals())
def edit_passenger(request, id_passenger):
    passenger = Passenger.objects.get(passenger_id=id_passenger)
    form = Passenger_Form(instance=passenger)
    if request.method == "POST":
        form = Passenger_Form(request.POST, instance=passenger)
        if form.is_valid():
            form.save()
            return redirect('passenger')
        else:
            return render(request, 'passenger/edit_passenger.html', locals())
    return render(request, 'passenger/edit_passenger.html', locals())
def delete_passenger(request, id_passenger):
    passenger = Passenger.objects.get(passenger_id=id_passenger)
    if request.method == "POST":
        if 'yes' in request.POST.keys() and request.POST['yes']:
            passenger.delete()
            return redirect('passenger')
        else:
            return redirect("passenger")
    return render(request, "passenger/delete_passenger.html", locals())



def show_flight_conditions(request):
    flight_conditions_list = Flight_conditions.objects.all()
    return render(request, "flight_conditions/show_flight_conditions.html", locals())
def add_flight_conditions(request):
    form = Flight_conditions_Form()
    if request.method == "POST":
        form = Flight_conditions_Form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('flight_conditions')
        else:
            return render(request, "flight_conditions/add_flight_conditions.html", locals())
    return render(request, "flight_conditions/add_flight_conditions.html", locals())
def edit_flight_conditions(request, id_flight_conditions):
    flight_conditions = Flight_conditions.objects.get(flight_conditions_id=id_flight_conditions)
    form = Flight_conditions_Form(instance=flight_conditions)
    if request.method == "POST":
        form = Flight_conditions_Form(request.POST, instance=flight_conditions)
        if form.is_valid():
            form.save()
            return redirect('flight_conditions')
        else:
            return render(request, 'flight_conditions/edit_flight_conditions.html', locals())
    return render(request, 'flight_conditions/edit_flight_conditions.html', locals())
def delete_flight_conditions(request, id_flight_conditions):
    flight_conditions = Flight_conditions.objects.get(flight_conditions_id=id_flight_conditions)
    if request.method == "POST":
        if 'yes' in request.POST.keys() and request.POST['yes']:
            flight_conditions.delete()
            return redirect('flight_conditions')
        else:
            return redirect("flight_conditions")
    return render(request, "flight_conditions/delete_flight_conditions.html", locals())



def show_airports(request):
    airports_list = Airports.objects.all()
    return render(request, "airports/show_airports.html", locals())
def add_airports(request):
    form = Airports_Form()
    if request.method == "POST":
        form = Airports_Form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('airports')
        else:
            return render(request, "airports/add_airports.html", locals())
    return render(request, "airports/add_airports.html", locals())
def edit_airports(request, id_airports):
    airports = Airports.objects.get(airports_id=id_airports)
    form = Airports_Form(instance=airports)
    if request.method == "POST":
        form = Airports_Form(request.POST, instance=airports)
        if form.is_valid():
            form.save()
            return redirect('airports')
        else:
            return render(request, 'airports/edit_airports.html', locals())
    return render(request, 'airports/edit_airports.html', locals())
def delete_airports(request, id_airports):
    airports = Airports.objects.get(airports_id=id_airports)
    if request.method == "POST":
        if 'yes' in request.POST.keys() and request.POST['yes']:
            airports.delete()
            return redirect('airports')
        else:
            return redirect("airports")
    return render(request, "airports/delete_airports.html", locals())



def show_company(request):
    company_list = Company.objects.all()
    return render(request, "company/show_company.html", locals())
def add_company(request):
    form = Company_Form()
    if request.method == "POST":
        form = Company_Form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('company')
        else:
            return render(request, "company/add_company.html", locals())
    return render(request, "company/add_company.html", locals())
def edit_company(request, id_company):
    company = Company.objects.get(company_id=id_company)
    form = Company_Form(instance=company)
    if request.method == "POST":
        form = Company_Form(request.POST, instance=company)
        if form.is_valid():
            form.save()
            return redirect('company')
        else:
            return render(request, 'company/edit_company.html', locals())
    return render(request, 'company/edit_company.html', locals())
def delete_company(request, id_company):
    company = Company.objects.get(company_id=id_company)
    if request.method == "POST":
        if 'yes' in request.POST.keys() and request.POST['yes']:
            company.delete()
            return redirect('company')
        else:
            return redirect("company")
    return render(request, "company/delete_company.html", locals())


def show_model_aircraft(request):
    model_aircraft_list = Model_aircraft.objects.all()
    return render(request, "model_aircraft/show_model_aircraft.html", locals())
def add_model_aircraft(request):
    form = Model_aircraft_Form()
    if request.method == "POST":
        form = Model_aircraft_Form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('model_aircraft')
        else:
            return render(request, "model_aircraft/add_model_aircraft.html", locals())
    return render(request, "model_aircraft/add_model_aircraft.html", locals())
def edit_model_aircraft(request, id_model_aircraft):
    model_aircraft = Model_aircraft.objects.get(model_aircraft_id=id_model_aircraft)
    form = Model_aircraft_Form(instance=model_aircraft)
    if request.method == "POST":
        form = Model_aircraft_Form(request.POST, instance=model_aircraft)
        if form.is_valid():
            form.save()
            return redirect('model_aircraft')
        else:
            return render(request, 'model_aircraft/edit_model_aircraft.html', locals())
    return render(request, 'model_aircraft/edit_model_aircraft.html', locals())
def delete_model_aircraft(request, id_model_aircraft):
    model_aircraft = Model_aircraft.objects.get(model_aircraft_id=id_model_aircraft)
    if request.method == "POST":
        if 'yes' in request.POST.keys() and request.POST['yes']:
            model_aircraft.delete()
            return redirect('model_aircraft')
        else:
            return redirect("model_aircraft")
    return render(request, "model_aircraft/delete_model_aircraft.html", locals())



def show_aircrafts(request):
    aircrafts_list = Aircrafts.objects.all()
    return render(request, "aircrafts/show_aircrafts.html", locals())
def add_aircrafts(request):
    form = Aircrafts_Form()
    if request.method == "POST":
        form = Aircrafts_Form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('aircrafts')
        else:
            return render(request, "aircrafts/add_aircrafts.html", locals())
    return render(request, "aircrafts/add_aircrafts.html", locals())
def edit_aircrafts(request, id_aircrafts):
    aircrafts = Aircrafts.objects.get(aircrafts_id=id_aircrafts)
    form = Aircrafts_Form(instance=aircrafts)
    if request.method == "POST":
        form = Aircrafts_Form(request.POST, instance=aircrafts)
        if form.is_valid():
            form.save()
            return redirect('aircrafts')
        else:
            return render(request, 'aircrafts/edit_aircrafts.html', locals())
    return render(request, 'aircrafts/edit_aircrafts.html', locals())
def delete_aircrafts(request, id_aircrafts):
    aircrafts = Aircrafts.objects.get(aircrafts_id=id_aircrafts)
    if request.method == "POST":
        if 'yes' in request.POST.keys() and request.POST['yes']:
            aircrafts.delete()
            return redirect('aircrafts')
        else:
            return redirect("aircrafts")
    return render(request, "aircrafts/delete_aircrafts.html", locals())



def show_flight(request):
    flight_list = Flight.objects.all()
    return render(request, "flight/show_flight.html", locals())
def add_flight(request):
    form = Flights_Form()
    if request.method == "POST":
        form = Flights_Form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('flight')
        else:
            return render(request, "flight/add_flight.html", locals())
    return render(request, "flight/add_flight.html", locals())
def edit_flight(request, id_flight):
    flight = Flight.objects.get(flight_id=id_flight)
    form = Flights_Form(instance=flight)
    if request.method == "POST":
        form = Flights_Form(request.POST, instance=flight)
        if form.is_valid():
            form.save()
            return redirect('flight')
        else:
            return render(request, 'flight/edit_flight.html', locals())
    return render(request, 'flight/edit_flight.html', locals())
def delete_flight(request, id_flight):
    flight = Flight.objects.get(flight_id=id_flight)
    if request.method == "POST":
        if 'yes' in request.POST.keys() and request.POST['yes']:
            flight.delete()
            return redirect('flight')
        else:
            return redirect("flight")
    return render(request, "flight/delete_flight.html", locals())


def show_boarding_pass(request):
    boarding_pass_list = Boarding_pass.objects.all()
    return render(request, "boarding_pass/show_boarding_pass.html", locals())
def add_boarding_pass(request):
    form = Boarding_pass_Form()
    if request.method == "POST":
        form = Boarding_pass_Form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('boarding_pass')
        else:
            return render(request, "boarding_pass/add_boarding_pass.html", locals())
    return render(request, "boarding_pass/add_boarding_pass.html", locals())
def edit_boarding_pass(request, id_boarding_pass):
    boarding_pass = Boarding_pass.objects.get(boarding_pass_id=id_boarding_pass)
    form = Boarding_pass_Form(instance=boarding_pass)
    if request.method == "POST":
        form = Boarding_pass_Form(request.POST, instance=boarding_pass)
        if form.is_valid():
            form.save()
            return redirect('boarding_pass')
        else:
            return render(request, 'boarding_pass/edit_boarding_pass.html', locals())
    return render(request, 'boarding_pass/edit_boarding_pass.html', locals())
def delete_boarding_pass(request, id_boarding_pass):
    boarding_pass = Boarding_pass.objects.get(boarding_pass_id=id_boarding_pass)
    if request.method == "POST":
        if 'yes' in request.POST.keys() and request.POST['yes']:
            boarding_pass.delete()
            return redirect('boarding_pass')
        else:
            return redirect("boarding_pass")
    return render(request, "boarding_pass/delete_boarding_pass.html", locals())



def show_tickets(request):
    tickets_list = Tickets.objects.all()
    return render(request, "tickets/show_tickets.html", locals())
def add_tickets(request):
    form = Tickets_Form()
    if request.method == "POST":
        form = Tickets_Form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('tickets')
        else:
            return render(request, "tickets/add_tickets.html", locals())
    return render(request, "tickets/add_tickets.html", locals())
def edit_tickets(request, id_tickets):
    tickets = Tickets.objects.get(tickets_id=id_tickets)
    form = Tickets_Form(instance=tickets)
    if request.method == "POST":
        form = Tickets_Form(request.POST, instance=tickets)
        if form.is_valid():
            form.save()
            return redirect('tickets')
        else:
            return render(request, 'tickets/edit_tickets.html', locals())
    return render(request, 'tickets/edit_tickets.html', locals())
def delete_tickets(request, id_tickets):
    tickets = Tickets.objects.get(tickets_id=id_tickets)
    if request.method == "POST":
        if 'yes' in request.POST.keys() and request.POST['yes']:
            tickets.delete()
            return redirect('tickets')
        else:
            return redirect("tickets")
    return render(request, "tickets/delete_tickets.html", locals())



def show_staff(request):
    staff_list = Staff.objects.all()
    return render(request, "staff/show_staff.html", locals())
def add_staff(request):
    form = Staff_Form()
    if request.method == "POST":
        form = Staff_Form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('staff')
        else:
            return render(request, "staff/add_staff.html", locals())
    return render(request, "staff/add_staff.html", locals())
def edit_staff(request, id_staff):
    staff = Staff.objects.get(staff_id=id_staff)
    form = Staff_Form(instance=staff)
    if request.method == "POST":
        form = Staff_Form(request.POST, instance=staff)
        if form.is_valid():
            form.save()
            return redirect('staff')
        else:
            return render(request, 'staff/edit_staff.html', locals())
    return render(request, 'staff/edit_staff.html', locals())
def delete_staff(request, id_staff):
    staff = Staff.objects.get(staff_id=id_staff)
    if request.method == "POST":
        if 'yes' in request.POST.keys() and request.POST['yes']:
            staff.delete()
            return redirect('staff')
        else:
            return redirect("staff")
    return render(request, "staff/delete_staff.html", locals())






