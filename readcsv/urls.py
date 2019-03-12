from django.conf.urls import url
from readcsv import views

urlpatterns = [
    url(r'csvdata', views.ReadJson.as_view()),
    url(r'showdata', views.ShowJson.as_view()),
    url(r'callprocess', views.callprocess),
    url(r'writecsv', views.writecsv)
]