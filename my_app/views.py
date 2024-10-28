from django.shortcuts import render, redirect
from .models import Bike, Category

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
        category_id = request.POST.get('category')
        category = Category.objects.get(id=category_id)
        Bike.objects.create(brand=brand, model=model, description=description, category=category)
        return redirect('bike_index')
    categories = Category.objects.all()  # Fetch all categories
    return render(request, 'bikes/create.html', {'categories': categories})



# Update view - Update an existing bike
def update_bike(request, bike_id):
    bike = Bike.objects.get(id=bike_id)
    if request.method == 'POST':
        bike.brand = request.POST.get('brand')
        bike.model = request.POST.get('model')
        bike.description = request.POST.get('description')
        category_id = request.POST.get('category')
        bike.category = Category.objects.get(id=category_id) if category_id else None
        bike.save()
        return redirect('bike_detail', bike_id=bike.pk)
    categories = Category.objects.all()  # Fetch categories for the dropdown
    return render(request, 'bikes/update.html', {'bike': bike, 'categories': categories})

def add_category(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        Category.objects.create(name=name)
        return redirect('create_bike')  # Redirect back to the bike creation page
    return render(request, 'bikes/add_category.html')

# Delete view - Delete a bike
def delete_bike(request, bike_id):
    bike = Bike.objects.get(id=bike_id)
    if request.method == 'POST':
        bike.delete()
        return redirect('bike_index')
    return render(request, 'bikes/delete.html', {'bike': bike})
