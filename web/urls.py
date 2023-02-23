from . import views
from django.urls import path



app_name = "web"

urlpatterns = [
    path("", views.signin, name="signin"),
    path("signup/", views.signup, name="signup"),
    path("logout/", views.logout_page, name="logout_page"),
    path("add-question/", views.addQuestion, name="addQuestion"),
    path("home/", views.index, name="index"),
]