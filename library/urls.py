from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('records/', views.records, name='records'),
    path('records/<int:ad>/', views.details, name='details'),
    path('records/delete/<int:pk>/', views.delete, name='delete'),
    path('teachers/', views.teachers, name='teachers'),
    path('teachers/records/', views.teachers_records, name='teachers_records'),
    path('teachers/records/<int:ac>/', views.teachers_details, name='teacher_details'),
    path('teachers/records/delete/<int:ax>/', views.teacher_delete, name='teacher_delete'),
]