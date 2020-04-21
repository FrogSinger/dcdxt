from django.conf.urls import url
from coursePerson import views

urlpatterns = [
    url(r'^index',views.index),
    url(r'^course_value$', views.course_value),
    url(r'^get_examine$', views.get_examine),
    url(r'^course_examine$', views.course_examine),
    url(r'^examine$', views.examine),
]