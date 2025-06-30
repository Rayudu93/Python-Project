# health/views.py
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Patient

class PatientListView(ListView):
    model = Patient
    context_object_name = 'patients'
    template_name = 'health/patient_list.html'

class PatientDetailView(DetailView):
    model = Patient
    context_object_name = 'patient'
    template_name = 'health/patient_detail.html'

class PatientCreateView(CreateView):
    model = Patient
    fields = '__all__'
    template_name = 'health/patient_form.html'
    success_url = reverse_lazy('patient_list')

class PatientUpdateView(UpdateView):
    model = Patient
    fields = '__all__'
    template_name = 'health/patient_form.html'
    success_url = reverse_lazy('patient_list')

class PatientDeleteView(DeleteView):
    model = Patient
    template_name = 'health/patient_confirm_delete.html'
    success_url = reverse_lazy('patient_list')
