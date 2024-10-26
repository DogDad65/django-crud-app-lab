from django.shortcuts import render, redirect
from .models import Bike

# Home view
def home(request):
    return render(request, 'bikes/home.html')


# Index view - List all bikes
def bike_index(request):
    bikes = Bike.objects.all()
    return render(request, 'bikes/index.html', {'bikes': bikes})

# Detail view - Show details of a single bike
def bike_detail(request, bike_id):
    bike = Bike.objects.get(id=bike_id)
    return render(request, 'bikes/detail.html', {'bike': bike})

# Create view - Create a new bike
def create_bike(request):
    if request.method == 'POST':
        brand = request.POST.get('brand')
        model = request.POST.get('model')
        description = request.POST.get('description')
        Bike.objects.create(brand=brand, model=model, description=description)
        return redirect('bike_index')
    return render(request, 'bikes/create.html')

# Update view - Update an existing bike
def update_bike(request, bike_id):
    bike = Bike.objects.get(id=bike_id)
    if request.method == 'POST':
        bike.brand = request.POST.get('brand')
        bike.model = request.POST.get('model')
        bike.description = request.POST.get('description')
        bike.save()
        return redirect('bike_detail', bike_id=bike.pk)  # Use pk instead of id
    return render(request, 'bikes/update.html', {'bike': bike})



# Delete view - Delete a bike
def delete_bike(request, bike_id):
    bike = Bike.objects.get(id=bike_id)
    if request.method == 'POST':
        bike.delete()
        return redirect('bike_index')
    return render(request, 'bikes/delete.html', {'bike': bike})
