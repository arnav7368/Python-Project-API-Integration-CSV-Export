from django.urls import path
from myapp import views

urlpatterns = [
    path('', views.index, name='index'),
    path('download/', views.download_csv, name='download_csv'),
]
