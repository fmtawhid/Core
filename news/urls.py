from django.urls import path
from .views import *
urlpatterns = [
    path('', news),
    path('<int:id>/', singlenews, name='sn'),
]