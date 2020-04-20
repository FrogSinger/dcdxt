from django.conf.urls import url
from coursePerson import views

urlpatterns = [
    url(r'^index',views.index),
    url(r'^get_examine$', views.get_examine),
    url(r'^course_examine$', views.course_examine),
]