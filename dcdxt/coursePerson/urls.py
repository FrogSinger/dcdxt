from django.conf.urls import url
from coursePerson import views

urlpatterns = [
    url(r'^index',views.index),
    url(r'^get_examine$', views.get_examine),
]