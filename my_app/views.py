from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Bike, Category, Maintenance
from .forms import MaintenanceForm

def home(request):
    return render(request, 'bikes/home.html')

def add_category(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        Category.objects.create(name=name)
        return redirect('create_bike')  # Redirect back to the bike creation page after adding category
    return render(request, 'bikes/add_category.html')

class BikeListView(ListView):
    model = Bike
    template_name = 'bikes/index.html'
    context_object_name = 'bikes'

class BikeDetailView(DetailView):
    model = Bike
    template_name = 'bikes/detail.html'
    context_object_name = 'bike'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['maintenance_form'] = MaintenanceForm()  # Pass the maintenance form to the template
        return context

class BikeCreateView(CreateView):
    model = Bike
    fields = ['brand', 'model', 'description', 'category']
    template_name = 'bikes/create.html'
    success_url = reverse_lazy('bike_index')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        return context

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

class BikeDeleteView(DeleteView):
    model = Bike
    template_name = 'bikes/delete.html'
    success_url = reverse_lazy('bike_index')

# Add the new view function here
def add_maintenance(request, bike_id):
    bike = get_object_or_404(Bike, id=bike_id)
    if request.method == 'POST':
        form = MaintenanceForm(request.POST)
        if form.is_valid():
            new_maintenance = form.save(commit=False)
            new_maintenance.bike = bike
            new_maintenance.save()
        return redirect('bike_detail', pk=bike.id)
