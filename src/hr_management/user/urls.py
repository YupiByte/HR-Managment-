from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("manage_employees/", views.manage_employees, name="manage_employees"), # <========== video equivalent to path('', views.home)
    path('admin_home/', views.admin_home, name='admin_home'), 
    path('tmp/', views.tmp, name='tmp'),
    path('create_employee/', views.create_employee, name='create_employee'),
    path('create/', views.create_employee, name='create_employee'),
    path('employee_record/<int:pk>', views.employee_record, name='employee_record'),
    path('delete_employee/<int:pk>', views.delete_employee, name='delete_employee'),
]

'''
urlpatterns = [
    path('', views.home, name='home'),
    #path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('register/', views.register_user, name='register'),
    path('record/<int:pk>', views.customer_record, name='record'),
    path('delete_record/<int:pk>', views.delete_record, name='delete_record'),
    path('add_record/', views.add_record, name='add_record'),
    path('update_record/<int:pk>', views.update_record, name='update_record'),

]
'''