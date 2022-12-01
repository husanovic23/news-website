from django.urls import path
from .views import base,contact,single,category,main,BaseDetailview

urlpatterns = [
    path('',main),
    path('contact',contact,name='cont'),
    path('category',category,name='cat'),
    path('single',single,name='single'),
    path('news_d/<int:pk>/',BaseDetailview.as_view(), name='news_d')
]