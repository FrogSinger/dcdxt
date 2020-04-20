from django.conf.urls import url
from teacher import views

urlpatterns = [
    url(r'^index$',views.index),
    url(r'^import_course$',views.import_course),
    url(r'^import_course_data$',views.import_course_data),
    url(r'^get_course_data$', views.get_course_data),
    url(r'^get_value_data$', views.get_value_data),
    url(r'^download_course_template$', views.download_course_template)
]