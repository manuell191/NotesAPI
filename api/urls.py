from django.urls import path
from . import views

urlpatterns = [
    path('', views.getRoutes),
    path('user', views.profiles),
    path('user/<pk>', views.profile),
    path('user/<pk>/notes', views.userNotes),
    path('note', views.notes),
    path('note/<pk>', views.note),
    path('login', views.login)
]
