from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Bike, Category, Maintenance, Upgrade
from .forms import MaintenanceForm, UpgradeForm

# Home view
def home(request):
    return render(request, 'bikes/home.html')

# Add Category view
def add_category(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        Category.objects.create(name=name)
        return redirect('bike_index')
    return render(request, 'bikes/add_category.html')

def create_bike(request):
    categories = Category.objects.all()  # Fetch categories for the dropdown
    bikes = Bike.objects.all()           # Fetch bikes to display in the list

    if request.method == 'POST':
        # Handle form submission here (save new bike, etc.)
        pass

    return render(request, 'bikes/create.html', {'categories': categories, 'bikes': bikes})

# Add Maintenance view (newly defined function)
def add_maintenance(request, bike_id):
    bike = get_object_or_404(Bike, id=bike_id)
    if request.method == 'POST':
        form = MaintenanceForm(request.POST)
        if form.is_valid():
            maintenance = form.save(commit=False)
            maintenance.bike = bike
            maintenance.save()
            return redirect('bike_detail', pk=bike_id)
    else:
        form = MaintenanceForm()
    return render(request, 'bikes/add_maintenance.html', {'form': form, 'bike': bike})

# List of Bikes
class BikeListView(ListView):
    model = Bike
    template_name = 'bikes/index.html'
    context_object_name = 'bikes'

# Detailed view of a Bike with inline forms for adding maintenance and upgrades
class BikeDetailView(DetailView):
    model = Bike
    template_name = 'bikes/detail.html'
    context_object_name = 'bike'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['upgrade_form'] = UpgradeForm()  # Form for adding an upgrade
        context['maintenance_form'] = MaintenanceForm()  # Form for adding maintenance
        context['upgrades'] = Upgrade.objects.filter(bike=self.object)
        context['maintenance_records'] = Maintenance.objects.filter(bike=self.object)
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        maintenance_form = MaintenanceForm(request.POST)
        upgrade_form = UpgradeForm(request.POST)

        if 'add_maintenance' in request.POST and maintenance_form.is_valid():
            maintenance = maintenance_form.save(commit=False)
            maintenance.bike = self.object
            maintenance.save()
        elif 'add_upgrade' in request.POST and upgrade_form.is_valid():
            upgrade = upgrade_form.save(commit=False)
            upgrade.bike = self.object
            upgrade.save()

        return redirect('bike_detail', pk=self.object.pk)

# Create a new Bike
class BikeCreateView(CreateView):
    model = Bike
    fields = ['brand', 'model', 'description', 'category']
    template_name = 'bikes/create.html'
    success_url = reverse_lazy('bike_index')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        return context

# Update an existing Bike
class BikeUpdateView(UpdateView):
    model = Bike
    fields = ['brand', 'model', 'description', 'category']
    template_name = 'bikes/update.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        return context

    def get_success_url(self):
        return reverse_lazy('bike_detail', kwargs={'pk': self.object.pk})

# Delete a Bike
class BikeDeleteView(DeleteView):
    model = Bike
    template_name = 'bikes/delete.html'
    success_url = reverse_lazy('bike_index')

# Upgrade views
class UpgradeListView(ListView):
    model = Upgrade
    template_name = 'upgrades/upgrade_list.html'  # Updated to match the actual template
    context_object_name = 'upgrades'


class UpgradeDetailView(DetailView):
    model = Upgrade
    template_name = 'upgrades/upgrade_detail.html'
    context_object_name = 'upgrade'

class UpgradeCreateView(CreateView):
    model = Upgrade
    form_class = UpgradeForm
    template_name = 'upgrades/upgrade_form.html'
    success_url = reverse_lazy('upgrade_list')


class UpgradeUpdateView(UpdateView):
    model = Upgrade
    form_class = UpgradeForm
    template_name = 'upgrades/upgrade_form.html'
    success_url = reverse_lazy('upgrade_list')

class UpgradeDeleteView(DeleteView):
    model = Upgrade
    template_name = 'upgrades/upgrade_confirm_delete.html'
    success_url = reverse_lazy('upgrade_list')
