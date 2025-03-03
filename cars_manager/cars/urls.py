from django.urls import path
from cars.views import car_list, add_car, move_car, delete_car

urlpatterns = [
    path('', car_list, name='car_list'),
    path('add/', add_car, name='add_car'),
    path('move/<int:car_id>/', move_car, name='move_car'),
    path('delete/<int:car_id>/', delete_car, name='delete_car'),
]
