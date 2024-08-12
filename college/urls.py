from django.urls import path
from . import views

urlpatterns = [
    path('add_course/', views.add_course, name='add_course'),  
    path('courses/', views.course_list, name='course_list'),
    path('students/', views.student_list, name='student_list'),
    path('course/edit/<int:pk>/', views.edit_course, name='edit_course'),
    path('course/delete/<int:pk>/', views.delete_course, name='delete_course'),
    path('', views.home, name='home'),
]
