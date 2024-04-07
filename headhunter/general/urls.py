from django.urls import path
from . import views
from django.urls import path, include

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:vacancies_id>/job', views.jobconnect, name='jobconnect'),
    path('<int:vacancies_id>/jobreject', views.jobreject, name='jobreject'),
    path('<int:position_id>/invite', views.invite, name='invite'),
    path('<int:position_id>/reject', views.reject, name='reject')
    # path('about/', views.about, name='about')
]
