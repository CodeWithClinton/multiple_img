from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name = "index"),
    path("create_project", views.create_product, name='create'),
    path("product/<str:id>", views.detail, name = 'detail')
]
