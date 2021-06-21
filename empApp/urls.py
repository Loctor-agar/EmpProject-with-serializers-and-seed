from django.urls import path

from . import views

urlpatterns = [
    path('append/', views.emp_list),

]
