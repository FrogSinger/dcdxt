from django.conf.urls import url
from majorPerson import views

urlpatterns = [
    url(r'^index',views.index),
    url(r'import_data$',views.import_data),
    url(r'get_matrix$', views.get_matrix),
]