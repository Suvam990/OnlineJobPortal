from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='job_list'),
    path('apply/<slug:slug>/', views.apply_for_job, name='apply_for_job'),
    path('home/', views.home, name='home'),
    path('category/<slug:slug>/', views.category_jobs, name='category_jobs'),
   
]
