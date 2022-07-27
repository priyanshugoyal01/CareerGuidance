from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('quiz/', views.quiz, name='quiz'),
    path('interest/', views.InterestList.as_view(), name='interest-list'),
    path('branch/', views.BranchList.as_view(), name='branch-list'),
    path('college/', views.CollegeList.as_view(), name='college-list'),

]
