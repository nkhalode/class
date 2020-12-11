
from django.urls import path
from stand import views

urlpatterns = [
    path('', views.BlogView),
]
