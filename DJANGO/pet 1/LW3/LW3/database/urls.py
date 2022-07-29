from django.conf.urls import url, include
from database import views

urlpatterns = [
    url(r"^main_menu/", views.main_menu, name="main_menu"),

    # URL providers
    url(r"^provider/$", views.show_provider, name="provider"),
    url(r"^edit_provider/(?P<id_provider>\d+)$", views.edit_provider, name="edit_provider"),
    url(r"^delete_provider/(?P<id_provider>\d+)$", views.delete_provider, name="delete_provider"),
    url(r"^add_provider/$", views.add_provider, name="add_provider"),

    # URL firms
    url(r"^firm/$", views.show_firm, name="firm"),
    url(r"^edit_firm/(?P<id_firm>\d+)$", views.edit_firm, name="edit_firm"),
    url(r"^delete_firm/(?P<id_firm>\d+)$", views.delete_firm, name="delete_firm"),
    url(r"^add_firm/$", views.add_firm, name="add_firm"),

    # URL sellers
    url(r"^seller/$", views.show_seller, name="seller"),
    url(r"^edit_seller/(?P<id_seller>\d+)$", views.edit_seller, name="edit_seller"),
    url(r"^delete_seller/(?P<id_seller>\d+)$", views.delete_seller, name="delete_seller"),
    url(r"^add_seller/$", views.add_seller, name="add_seller"),

    # URL equipment type
    url(r"^type/$", views.show_type, name="type"),
    url(r"^edit_type/(?P<id_type>\d+)$", views.edit_type, name="edit_type"),
    url(r"^delete_type/(?P<id_type>\d+)$", views.delete_type, name="delete_type"),
    url(r"^add_type/$", views.add_type, name="add_type"),

    # URL equipment
    url(r"^equipment/$", views.show_equipment, name="equipment"),
    url(r"^edit_equipment/(?P<id_equipment>\d+)$", views.edit_equipment, name="edit_equipment"),
    url(r"^delete_equipment/(?P<id_equipment>\d+)$", views.delete_equipment, name="delete_equipment"),
    url(r"^add_equipment/$", views.add_equipment, name="add_equipment"),
]


