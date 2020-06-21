from django.urls import path
from bts import views

app_name = 'bts'

urlpatterns = [
    path('', views.index, name='index'),
    path('new_release/', views.new_release, name='new release'),
    ]
