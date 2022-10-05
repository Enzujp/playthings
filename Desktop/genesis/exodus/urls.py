from django.urls import path

from . import views

app_name = 'exodus'

urlpatterns= [
    path('', views.index, name="index",
    )
]