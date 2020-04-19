from django.conf.urls import url
from teacher import views

urlpatterns = [
    url(r'^index',views.index),
    url(r'^import_course_data$',views.import_course_data),
]