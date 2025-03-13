from django.shortcuts import render, get_object_or_404, redirect
from cars.models import Car
from django.db.models import Max

def car_list(request):
    """Display a list of cars with optional color filtering"""
    color = request.GET.get('color', '')

    # Get unique colors correctly
    colors = Car.objects.order_by('color').values_list('color', flat=True).distinct()

    # Filter cars by color (regardless of position)
    cars = Car.objects.all()
    if color:
        cars = cars.filter(color=color)

    # Ensure sorted by position
    cars = cars.order_by('position')

    return render(request, 'cars/car_list.html', {'cars': cars, 'colors': colors, 'selected_color': color})

def move_car(request, car_id):
    """Move a car to a new position"""
    car = get_object_or_404(Car, id=car_id)

    if request.method == 'POST':
        new_position = float(request.POST['new_position'])

        # Shift cars if necessary
        if Car.objects.filter(position=new_position).exists():
            Car.objects.filter(position__gte=new_position).update(position=Max('position') + 1)

        car.position = new_position
        car.save()

    return redirect('car_list')

def add_car(request):
    """Add a new car to the list"""
    if request.method == 'POST':
        name = request.POST['name']
        color = request.POST['color']

        # Find the next available position
        max_position = Car.objects.aggregate(max_pos=Max('position'))['max_pos'] or 0
        new_position = max_position + 1

        Car.objects.create(name=name, color=color, position=new_position)

    return redirect('car_list')

def delete_car(request, car_id):
    """Delete a car"""
    car = get_object_or_404(Car, id=car_id)
    car.delete()
    return redirect('car_list')