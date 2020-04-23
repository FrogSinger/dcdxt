from django.conf.urls import url
from student import views

urlpatterns = [
    url(r'^index',views.index),
    url(r'^calculate_point_mark$',views.calculate_point_mark)
]