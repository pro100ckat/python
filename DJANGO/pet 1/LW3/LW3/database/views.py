from django.shortcuts import render, redirect
from database.forms import *
from database.models import *


def main_menu(request):
    return render(request, "main.html", locals())

#PROVIDERS VIEWS
def show_provider(request):
    provider_list = Provider.objects.all()
    return render(request, "provider/show_provider.html", locals())

def edit_provider(request, id_provider):
    provider = Provider.objects.get(provider_id=id_provider)
    form = Provider_Form(instance=provider)
    if request.method == "POST":
        form = Provider_Form(request.POST, instance=provider)
        if form.is_valid():
            form.save()
            return redirect('provider')
        else:
            return render(request, "provider/edit_provider.html", locals())
    return render(request, "provider/edit_provider.html", locals())

def delete_provider(request, id_provider):
    provider = Provider.objects.get(provider_id=id_provider)
    if request.method == "POST":
        if 'yes' in request.POST.keys() and request.POST['yes']:
            provider.delete()
            return redirect('provider')
        else:
            return redirect("provider")
    return render(request, 'provider/delete_provider.html', locals())

def add_provider(request):
    form = Provider_Form()
    if request.method == "POST":
        form = Provider_Form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('provider')
        else:
            return render(request, "provider/add_provider.html", locals())
    return render(request, "provider/add_provider.html", locals())

#FIRMS VIEWS
def show_firm(request):
    firm_list = Firm.objects.all()
    return render(request, "firm/show_firm.html", locals())

def edit_firm(request, id_firm):
    firm = Firm.objects.get(firm_id=id_firm)
    form = Firm_Form(instance=firm)
    if request.method == "POST":
        form = Firm_Form(request.POST, instance=firm)
        if form.is_valid():
            form.save()
            return redirect('firm')
        else:
            return render(request, "firm/edit_firm.html", locals())
    return render(request, "firm/edit_firm.html", locals())

def delete_firm(request, id_firm):
    firm = Firm.objects.get(firm_id=id_firm)
    if request.method == "POST":
        if 'yes' in request.POST.keys() and request.POST['yes']:
            firm.delete()
            return redirect("firm")
        else:
            return redirect("firm")
    return render(request, 'firm/delete_firm.html', locals())

def add_firm(request):
    form = Firm_Form()
    if request.method == "POST":
        form = Firm_Form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('firm')
        else:
            return render(request, "firm/add_firm.html", locals())
    return render(request, "firm/add_firm.html", locals())

#SELLER VIEWS
def show_seller(request):
    seller_list = Seller.objects.all()
    return render(request, "seller/show_seller.html", locals())

def edit_seller(request, id_seller):
    seller = Seller.objects.get(seller_id=id_seller)
    form = Seller_Form(instance=seller)
    if request.method == "POST":
        form = Seller_Form(request.POST, instance=seller)
        if form.is_valid():
            form.save()
            return redirect('seller')
        else:
            return render(request, "seller/edit_seller.html", locals())
    return render(request, "seller/edit_seller.html", locals())

def delete_seller(request, id_seller):
    seller = Seller.objects.get(seller_id=id_seller)
    if request.method == "POST":
        if 'yes' in request.POST.keys() and request.POST['yes']:
            seller.delete()
            return redirect("seller")
        else:
            return redirect("seller")
    return render(request, 'seller/delete_seller.html', locals())

def add_seller(request):
    form = Seller_Form()
    if request.method == "POST":
        form = Seller_Form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('seller')
        else:
            return render(request, "seller/add_seller.html", locals())
    return render(request, "seller/add_seller.html", locals())


#TYPE VIEWS
def show_type(request):
    type_list = Equipment_type.objects.all()
    return render(request, "type/show_type.html", locals())

def edit_type(request, id_type):
    etype = Equipment_type.objects.get(et_id=id_type)
    form = Type_Form(instance=etype)
    if request.method == "POST":
        form = Type_Form(request.POST, instance=etype)
        if form.is_valid():
            form.save()
            return redirect('type')
        else:
            return render(request, "type/edit_type.html", locals())
    return render(request, "type/edit_type.html", locals())

def delete_type(request, id_type):
    etype = Equipment_type.objects.get(et_id=id_type)
    if request.method == "POST":
        if 'yes' in request.POST.keys() and request.POST['yes']:
            etype.delete()
            return redirect("type")
        else:
            return redirect("type")
    return render(request, 'type/delete_type.html', locals())

def add_type(request):
    form = Type_Form()
    if request.method == "POST":
        form = Type_Form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('type')
        else:
            return render(request, "type/add_type.html", locals())
    return render(request, "type/add_type.html", locals())


#EQUIPMENT VIEWS

def show_equipment(request):
    equipment_list = Equipment.objects.all()
    return render(request, "equipment/show_equipment.html", locals())

def edit_equipment(request, id_equipment):
    equipment = Equipment.objects.get(equipment_id=id_equipment)
    form = Equipment_Form(instance=equipment)
    if request.method == "POST":
        form = Equipment_Form(request.POST, instance=equipment)
        if form.is_valid():
            form.save()
            return redirect('equipment')
        else:
            return render(request, "equipment/edit_equipment.html", locals())
    return render(request, "equipment/edit_equipment.html", locals())

def delete_equipment(request, id_equipment):
    equipment = Equipment.objects.get(equipment_id=id_equipment)
    if request.method == "POST":
        if 'yes' in request.POST.keys() and request.POST['yes']:
            equipment.delete()
            return redirect("equipment")
        else:
            return redirect("equipment")
    return render(request, 'equipment/delete_equipment.html', locals())

def add_equipment(request):
    form = Equipment_Form()
    if request.method == "POST":
        form = Equipment_Form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('equipment')
        else:
            return render(request, "equipment/add_equipment.html", locals())
    return render(request, "equipment/add_equipment.html", locals())
