from django.urls import path

from new_app import views

urlpatterns = [
    path("new",views.new,name='new')
]