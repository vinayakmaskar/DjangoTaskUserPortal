
from django.urls import path
from . import views

urlpatterns = [

    path("register",views.UserActions.as_view()),
    path('login', views.post_login_details, name='another-action'),
]
