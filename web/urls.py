from . import views
from django.urls import path



app_name = "web"

urlpatterns = [
    path("", views.signup, name="signup"),
    path("signin/", views.signin, name="signin"),
    path("logout/", views.logout, name="logout"),
    path("home/", views.index, name="index"),
]