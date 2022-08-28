from array import array
from django.urls import path, re_path
from app import views

apis = [
    path('login/', views.Login.as_view()),
    path('sign-up/', views.SignUp.as_view()),
    path('articles/', views.Articles.as_view()),
    re_path(r'^articles/(\d+)/$', views.ArticleDetail.as_view()),
]

admins = [
    path('articles/', views.Articles.as_view()),
    path('authors/', views.Authors.as_view()),
]