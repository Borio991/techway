from django.urls import path, include
from . import views


urlpatterns = [
    path('create/', views.create, name='create'),
    path('view/', views.view, name='view'),
    path('project/info/<int:pk>', views.view_project),
]
