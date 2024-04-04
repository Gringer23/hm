from django.urls import path
from . import views
from django.urls import path, include

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:vacancies_id>/job', views.jobconnect, name='jobconnect')
    # path('about/', views.about, name='about')
]
