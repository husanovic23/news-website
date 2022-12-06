from django.urls import path
from .views import *

urlpatterns = [
    path('',main),
        
    path('contact',contact,name='cont'),
    path('category',category,name='cat'),
    path('single',single,name='single'),
    path('news_d/<int:pk>/',BaseDetailview.as_view(), name='news_d'),
    path('cate_det/<int:pk>/',CategoryDetail.as_view(),name='cate_det'),
    path('serach/',Serachview.as_view(),name='serach'),


]
