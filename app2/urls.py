from django.urls import path

app_name='app2'
from app2 import views

urlpatterns=[
    path('hello/',views.hello,name='hello'),
]