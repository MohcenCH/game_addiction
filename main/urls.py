from django.urls import path
from main.views import *

urlpatterns = [
    path("login/", CustomLogin.as_view(), name="login"),
]
