from django.urls import path
from . import views

urlpatterns=[
    path('load/',views.app_method,name='app_me'),
    path('',views.home,name='Home'),
    path('app/',views.app,name="loader"),
    path('student/',views.students,name="output"),
    path('app/form/',views.form,name='form'),
    path('post/<id>',views.post,name="post"),
]