from django.urls import path
from equipointervalo.views import *

urlpatterns = [
    path("", index, name="index"),
    path('profesionales/', profesionales, name="profesionales"),
    path('areas/', areas, name="areas"),
    path('servicios/', servicios, name="servicios"),
]
