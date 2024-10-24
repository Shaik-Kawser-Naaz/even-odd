from django.urls import path
from app1 import views

urlpatterns=[
    path('num',views.func1,name="numform")
]