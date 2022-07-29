from django.forms import ModelForm
from excelapp.models import *

class FilesForm(ModelForm):
  class Meta:
    model = Files
    fields = ["file_id", "file"]
    labels = {
        "file_id": "ID",
        "file": "Путь/Название",
    }

# class Napravlenie_Form(ModelForm):
#     class Meta:
#         model = Napravlenie
#         fields = ["napravlenie_name", "profil", "kvalification", "code", "napravlenie_date"]
#         labels = {
#             "napravlenie_name": "Наименование должности",
#             "profil": "Уровень доступа",
#             "kvalification": "Уровень доступа",
#             "code": "Уровень доступа",
#             "napravlenie_date": "Уровень доступа",
#                 }
#
# class UchPlan_Form(ModelForm):
#     class Meta:
#         model = UchPlan
#         fields = ["god_start", "protocol", "date_protocol", "kafedra", "uchplan_profil", "facultet"]
#         labels = {
#             "god_start": "Наименование должности",
#             "protocol": "Уровень доступа",
#             "date_protocol": "Уровень доступа",
#             "kafedra": "Уровень доступа",
#             "uchplan_profil": "Уровень доступа",
#             "facultet": "Уровень доступа",
#         }
#
# class Vidy_deyt_Form(ModelForm):
#     class Meta:
#         model = Vidy_deyt
#         fields = ["Vidy_deyt_name", "id_napravlenie"]
#         labels = {
#             "Vidy_deyt_name": "Виде деяткльности",
#             "id_napravlenie": "Направление",
#         }