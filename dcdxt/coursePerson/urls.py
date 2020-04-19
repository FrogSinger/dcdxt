from django.conf.urls import url
from coursePerson import views

urlpatterns = [
    url(r'^index',views.index),
]