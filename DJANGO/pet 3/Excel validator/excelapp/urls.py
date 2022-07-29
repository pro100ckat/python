from django.conf.urls import url
from excelapp import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
	url(r'^login/$', views.login, name="login"),
    url(r'^main_page/$', views.main_page, name="main_page"),
    url(r"^about/$", views.about, name="about"),
    url(r"^check_one/(?P<file_id>\d+)$", views.check_one, name='check_one'),
    url(r"^check/$", views.check, name='check'),
    url(r"^delete_file/(?P<file_id>\d+)$", views.delete_file, name="delete_file"),
    url(r'^clear_all/$', views.clear_all, name='clear_all'),
    url(r'^upload/$', views.upload.as_view(), name='upload'),
    url(r'^show/$', views.show, name='show'),
    url(r'^delete/$', views.delete, name='delete'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)