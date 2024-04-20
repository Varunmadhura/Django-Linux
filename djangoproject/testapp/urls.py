from django.urls import path
from testapp import views

urlpatterns = [
    path('', views.user_login, name='login'),
    path('scenario/', views.scenario, name='scenario'),
    path('execute_command/', views.execute_command, name='execute_command')
]
