from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
urlpatterns = [
    path('admin/', admin.site.urls),

    path('', TemplateView.as_view(template_name='base.html'), name='home'),

    path('catalog/', include('catalog.urls')),
    path('courses/', include('courses.urls')),
    path('jobs/', include('jobs.urls')),
    path('health/', include('health.urls')),
]
