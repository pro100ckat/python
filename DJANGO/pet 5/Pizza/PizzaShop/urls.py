from django.conf.urls import url
from PizzaShop import views
urlpatterns = [
  url(r'^main_menu/$', views.index, name="main_menu"),
  url(r'^contacts/$', views.contacts, name="contacts"),
  url(r'^pizza/$', views.pizza, name="pizza"),

  ]
