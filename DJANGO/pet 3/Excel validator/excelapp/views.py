from excelapp.forms import *
from excelapp.models import *
from django.shortcuts import render
from django.shortcuts import redirect
from excelapp.check import *
from django.http import JsonResponse
from django.views import View
from django.contrib import auth


un = '1'
pw = '2'

def login(request):
    if request.method == "POST":
        global un
        global pw
        un = request.POST['email']
        pw = request.POST['pass']
        user = auth.authenticate(username=un, password=pw)
        if user is not None:
            return redirect('main_page')
        else:
            return redirect('login')
    return render(request, "login.html", locals())


def main_page(req):
    user = auth.authenticate(username=un, password=pw)
    if user is not None:
        return render(req, 'main_page.html', locals())
    else:
        return redirect('auth')
	
def about(req):
    return render(req, 'about.html', locals())

def check_one(req, file_id):
    file = Files.objects.get(file_id=file_id)
    if req.method == "GET":
        return render(req, "check_one.html", locals())
    if req.method == "POST":
        if 'edit' not in req.POST:
            if 'titul' in req.POST:
                check_titul(req, file, shab=req.FILES['shablon'])
                file = Files.objects.get(file_id=file_id)
            if 'all' in req.POST:
                check_all(req, file,shab=req.FILES['shablon'])
                file = Files.objects.get(file_id=file_id)
            if 'grafik' in req.POST:
                check_grafik(req, file,shab=req.FILES['shablon'])
                file = Files.objects.get(file_id=file_id)
            if 'plan' in req.POST:
                check_plan(req, file,shab=req.FILES['shablon'])
                file = Files.objects.get(file_id=file_id)
            if 'plan_svod' in req.POST:
                check_plan_svod(req, file,shab=req.FILES['shablon'])
                file = Files.objects.get(file_id=file_id)
            if 'comp' in req.POST:
                check_compititions(req, file,shab=req.FILES['shablon'])
                file = Files.objects.get(file_id=file_id)
        else:
            if 'edit' in req.POST:
                if 'titul' in req.POST:
                    edit_titul(req, file, shab=req.FILES['shablon'])
                    file = Files.objects.get(file_id=file_id)
                if 'all' in req.POST:
                    edit_all(req, file,shab=req.FILES['shablon'])
                    file = Files.objects.get(file_id=file_id)
                if 'grafik' in req.POST:
                    edit_grafik(req, file,shab=req.FILES['shablon'])
                    file = Files.objects.get(file_id=file_id)
                if 'plan' in req.POST:
                    edit_plan_svod(req, file,shab=req.FILES['shablon'])
                    file = Files.objects.get(file_id=file_id)
                if 'plan_svod' in req.POST:
                    edit_plan_svod(req, file,shab=req.FILES['shablon'])
                    file = Files.objects.get(file_id=file_id)
                if 'comp' in req.POST:
                    edit_compititions(req, file,shab=req.FILES['shablon'])
                    file = Files.objects.get(file_id=file_id)
        return render(req, "check_one.html", locals())
    else:
        return render(req, "check_one.html", locals())
def delete_file(request, file_id):
    file = Files.objects.get(file_id=file_id)
    name_delete = file.file
    if request.method == "POST":
        if 'delete' in request.POST.keys() and request.POST['delete']:
            file.delete()
            return redirect("show")
        else:
            return redirect("show")
    return render(request, 'file_delete.html', locals())

class upload(View):
    def get(self, request):
        files = Files.objects.all()
        return render(self.request, 'upload.html', locals())

    def post(self, request):
        form = FilesForm(self.request.POST, self.request.FILES)
        if form.is_valid():
            file = form.save()
            data = {'is_valid': True, 'id': file.file_id, 'name': file.file.name, 'url': file.file.url}
        else:
            data = {'is_valid': False}
        return JsonResponse(data)

def clear_all(request):
    for file in Files.objects.all():
        file.file.delete()
        file.delete()
    return redirect(request.POST.get('next'))

def show(request):
    files = Files.objects.all().order_by('file')
    return render(request, 'show.html', locals())

def delete(request):
    files = Files.objects.all().order_by('file')
    if request.method == 'POST':
        id_list = request.POST.getlist('checkbox')
        for file in id_list:
            Files.objects.get(file_id=file).delete()
    return render(request, 'show.html', locals())

def check(req):
    return render(req, "check.html", locals())