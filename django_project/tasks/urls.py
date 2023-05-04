from django.urls import path

from . import views
app_name = 'tasks'

urlpatterns = [
    path('list/', views.list, name='list'),
    path('new/', views.new_task, name='new'),
    path('update_task/', views.update_task, name='update_task'),
]
