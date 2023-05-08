from django.urls import path

from . import views
app_name = 'tasks'

urlpatterns = [
    path('list/', views.list, name='list'),
    path('new/', views.new_task, name='new'),
    path('<int:pk>/delete/', views.delete_task, name='delete'),
    path('<int:pk>/complete/', views.complete_task, name='complete'),
    path('<int:pk>/edit/', views.edit_task, name='edit'),
]
