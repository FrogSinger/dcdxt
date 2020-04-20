from django.conf.urls import url
from teacher import views

urlpatterns = [
    url(r'^import_course$',views.import_course),
    url(r'^import_course_data$',views.import_course_data),
]