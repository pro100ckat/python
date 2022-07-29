from django.shortcuts import render, redirect
from MyCar.models import *
from MyCar.forms import *
import time
# Create your views here.

def main_page(req):
    mark_list = Mark.objects.all()
    return render(req, "main_page.html", locals())

def auto(req):
    mark_list = Mark.objects.all()
    model_list = ModelCar.objects.all()
    return render(req, "autos.html", locals())

def model(req, model_id):
    car = ModelCar.objects.get(model_car_id=model_id)
    form = RentForm(initial={
        'id_model': car.model_car_id
    })
    if req.method == "POST":
        form = RentForm(req.POST, initial={
        'car': car
    })
        if form.is_valid():
            form.save()
            time.sleep(3)
            return redirect('main_page')
        else:
            return render(req, "model.html", locals())
    return render(req, "model.html", locals())

def tariff(req):
    how = 0
    tariff_list = Tariff.objects.all()
    return render(req, "tariff.html", locals())

def operators(req):
    operator_list = Operator.objects.all()
    return render(req, "operators.html", locals())

def about(req):
    return render(req, "about.html", locals())

def admin_menu(req):
    return render(req, "admin/admin_menu.html", locals())

def show_rent(req):
    rent_list = Rent.objects.all()
    return render(req, "admin/rent/show.html", locals())

def show_rank(req):
    rank_list = Rank.objects.all()
    return render(req, "admin/Rank/show.html", locals())

def show_mark(req):
    mark_list = Mark.objects.all()
    return render(req, "admin/Mark/show.html", locals())

def show_models(req, id_mark):
    mark = Mark.objects.get(mark_id=id_mark)
    model_list = ModelCar.objects.all()
    return render(req, "admin/Model/show.html", locals())

def show_fuel(req):
    fuel_list = Fuel.objects.all()
    return render(req, "admin/Fuel/show.html", locals())

def show_operator(req):
    operator_list = Operator.objects.all()
    return render(req, "admin/Operator/show.html", locals())

def show_tariffs(req):
    tariffs_list = Tariff.objects.all()
    return render(req, "admin/Tariff/show.html", locals())

def add_rank(req):
    form = RankForM()
    if req.method == "POST":
        form = RankForM(req.POST)
        if form.is_valid():
            form.save()
            return redirect('show_rank')
        else:
            return render(req, "admin/admin_add.html", locals())
    return render(req, "admin/admin_add.html", locals())

def add_mark(req):
    form = MarkForm()
    if req.method == "POST":
        form = MarkForm(req.POST)
        if form.is_valid():
            form.save()
            return redirect('show_mark')
        else:
            return render(req, "admin/admin_add.html", locals())
    return render(req, "admin/admin_add.html", locals())

def add_operator(req):
    form = OperatorForm()
    if req.method == "POST":
        form = OperatorForm(req.POST, req.FILES)
        if form.is_valid():
            form.save()
            return redirect('show_operator')
        else:
            return render(req, "admin/admin_add.html", locals())
    return render(req, "admin/admin_add.html", locals())

def add_tariff(req):
    form = TariffForm()
    if req.method == "POST":
        form = TariffForm(req.POST)
        if form.is_valid():
            form.save()
            return redirect('show_tariffs')
        else:
            return render(req, "admin/admin_add.html", locals())
    return render(req, "admin/admin_add.html", locals())

def add_fuel(req):
    form = FuelForm()
    if req.method == "POST":
        form = FuelForm(req.POST)
        if form.is_valid():
            form.save()
            return redirect('show_fuel')
        else:
            return render(req, "admin/admin_add.html", locals())
    return render(req, "admin/admin_add.html", locals())

def add_model(req):
    form = ModelForm()
    if req.method == "POST":
        form = ModelForm(req.POST, req.FILES)
        if form.is_valid():
            form.save()
            return redirect('admin_menu')
        else:
            return render(req, "admin/admin_add.html", locals())
    return render(req, "admin/admin_add.html", locals())

def edit_rank(req, rank_id):
    rank = Rank.objects.get(rank_id=rank_id)
    form = RankForM(instance=rank)
    if req.method == "POST":
        form = RankForM(req.POST, instance=rank)
        if form.is_valid():
            form.save()
            return redirect('show_rank')
        else:
            return render(req, "admin/admin_edit.html", locals())
    return render(req, "admin/admin_edit.html", locals())

def edit_mark(req, mark_id):

    mark = Mark.objects.get(mark_id=mark_id)
    form = MarkForm(instance=mark)
    if req.method == "POST":
        form = MarkForm(req.POST, instance=mark)
        if form.is_valid():
            form.save()
            return redirect('show_mark')
        else:
            return render(req, "admin/admin_edit.html", locals())
    return render(req, "admin/admin_edit.html", locals())

def edit_model(req, model_id):

    model = ModelCar.objects.get(model_car_id=model_id)
    form = ModelForm(instance=model)
    if req.method == "POST":
        form = MarkForm(req.POST, req.FILES, instance=model)
        if form.is_valid():
            form.save()
            return redirect('admin_menu')
        else:
            return render(req, "admin/admin_edit.html", locals())
    return render(req, "admin/admin_edit.html", locals())

def edit_tariff(req, tariff_id):
    tarif = Tariff.objects.get(tariff_id=tariff_id)
    form = TariffForm(instance=tarif)
    if req.method == "POST":
        form = TariffForm(req.POST, instance=tarif)
        if form.is_valid():
            form.save()
            return redirect('show_tariffs')
        else:
            return render(req, "admin/admin_edit.html", locals())
    return render(req, "admin/admin_edit.html", locals())

def edit_fuel(req, fuel_id):
    fuel = Fuel.objects.get(fuel_id=fuel_id)
    form = FuelForm(instance=fuel)
    if req.method == "POST":
        form = FuelForm(req.POST, instance=fuel)
        if form.is_valid():
            form.save()
            return redirect('show_fuel')
        else:
            return render(req, "admin/admin_edit.html", locals())
    return render(req, "admin/admin_edit.html", locals())

def edit_rent(req, rent_id):
    rent = Rent.objects.get(rent_id=rent_id)
    form = RentEditForm(instance=rent)
    if req.method == "POST":
        form = RentEditForm(req.POST, req.FILES, instance=rent)
        if form.is_valid():
            form.save()
            return redirect('show_rent')
        else:
            return render(req, "admin/admin_edit.html", locals())
    return render(req, "admin/admin_edit.html", locals())

def edit_operator(req, operator_id):
    operator = Operator.objects.get(operator_id=operator_id)
    form = OperatorForm(instance=operator)
    if req.method == "POST":
        form = OperatorForm(req.POST, req.FILES, instance=operator)
        if form.is_valid():
            form.save()
            return redirect('show_operator')
        else:
            return render(req, "admin/admin_edit.html", locals())
    return render(req, "admin/admin_edit.html", locals())

def delete_rent(request, rent_id):
    rent = Rent.objects.get(rent_id=rent_id)
    name_delete = rent.name
    if request.method == "POST":
        if 'yes' in request.POST.keys() and request.POST['yes']:
            rent.delete()
            return redirect("show_rent")
        else:
            return redirect("show_rent")
    return render(request, 'admin/admin_delete.html', locals())

def delete_rank(request, rank_id):
    rank = Rank.objects.get(rank_id=rank_id)
    name_delete = rank.name
    if request.method == "POST":
        if 'yes' in request.POST.keys() and request.POST['yes']:
            rank.delete()
            return redirect("show_rank")
        else:
            return redirect("show_rank")
    return render(request, 'admin/admin_delete.html', locals())

def delete_mark(request, mark_id):
    mark = Mark.objects.get(mark_id=mark_id)
    name_delete = mark.name
    if request.method == "POST":
        if 'yes' in request.POST.keys() and request.POST['yes']:
            mark.delete()
            return redirect("show_mark")
        else:
            return redirect("show_mark")
    return render(request, 'admin/admin_delete.html', locals())

def delete_operator(request, operator_id):
    operator = Operator.objects.get(operator_id=operator_id)
    name_delete = operator.name
    if request.method == "POST":
        if 'yes' in request.POST.keys() and request.POST['yes']:
            operator.delete()
            return redirect("show_operator")
        else:
            return redirect("show_operator")
    return render(request, 'admin/admin_delete.html', locals())

def delete_tariff(request, tariff_id):
    tariff = Tariff.objects.get(tariff_id=tariff_id)
    name_delete = tariff.name
    if request.method == "POST":
        if 'yes' in request.POST.keys() and request.POST['yes']:
            tariff.delete()
            return redirect("show_tariffs")
        else:
            return redirect("show_tariffs")
    return render(request, 'admin/admin_delete.html', locals())

def delete_fuel(request, fuel_id):
    fuel = Fuel.objects.get(fuel_id=fuel_id)
    name_delete = fuel.name
    if request.method == "POST":
        if 'yes' in request.POST.keys() and request.POST['yes']:
            fuel.delete()
            return redirect("show_fuel")
        else:
            return redirect("show_fuel")
    return render(request, 'admin/admin_delete.html', locals())

def delete_model(request, model_car_id):
    model = ModelCar.objects.get(model_car_id=model_car_id)
    name_delete = model.name
    if request.method == "POST":
        if 'yes' in request.POST.keys() and request.POST['yes']:
            model.delete()
            return redirect("show_mark")
        else:
            return redirect("show_mark")
    return render(request, 'admin/admin_delete.html', locals())