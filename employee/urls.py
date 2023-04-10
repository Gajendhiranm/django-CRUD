from django.urls import path
from employee import views

urlpatterns = [
    path('',views.employee_list),
    path('api/employee/<int:pk>',views.employee_detail),

]
