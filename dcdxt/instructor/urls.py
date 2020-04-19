from django.conf.urls import url
from instructor import views

urlpatterns = [
    url(r'^index',views.index),
]