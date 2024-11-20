from . import views
from django.urls import path

urlpatterns = [
   path("", views.buzz_list,name='buzz_list'),
   path("create/", views.buzz_create,name='buzz_create'),
   path("<int:buzz_id>/edit/", views.buzz_edit,name='buzz_edit'),
   path("<int:buzz_id>/delete/", views.buzz_delete,name='buzz_delete'),
   path("register/", views.register,name='register'),
   
] 
