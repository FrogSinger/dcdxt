from django.conf.urls import url
from majorPerson import views

urlpatterns = [
    url(r'^index',views.index),
    url(r'import_data$',views.import_data),
    url(r'import_data_interface$',views.import_data_interface),
    url(r'get_matrix$', views.get_matrix),
]
