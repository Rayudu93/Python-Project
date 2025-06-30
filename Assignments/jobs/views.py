# jobs/views.py
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Job

class JobListView(ListView):
    model = Job
    context_object_name = 'jobs'
    template_name = 'jobs/job_list.html'

class JobDetailView(DetailView):
    model = Job
    context_object_name = 'job'
    template_name = 'jobs/job_detail.html'

class JobCreateView(CreateView):
    model = Job
    fields = '__all__'
    template_name = 'jobs/job_form.html'
    success_url = reverse_lazy('job_list')

class JobUpdateView(UpdateView):
    model = Job
    fields = '__all__'
    template_name = 'jobs/job_form.html'
    success_url = reverse_lazy('job_list')

class JobDeleteView(DeleteView):
    model = Job
    template_name = 'jobs/job_confirm_delete.html'
    success_url = reverse_lazy('job_list')
