from django.contrib import admin
from django.urls import path, include
from . import views  # import your app and views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('create/', views.student_create, name='create'),
    path('success/', views.success_view, name='success'), 
    path('students/', views.student_list, name='student_list'),
    path('update/<int:id>/', views.student_update, name='student_update'),
    path('delete/<int:id>/', views.student_delete, name='student_delete'), # map root URL to index view
]

# helllo
