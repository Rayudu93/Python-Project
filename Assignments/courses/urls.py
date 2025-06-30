from django.urls import path
from .views import CourseCreateView, CourseListView, CourseDetailView

urlpatterns = [
    path('', CourseListView.as_view(), name='course_list'),
    path('add/', CourseCreateView.as_view(), name='course_add'),
    path('<int:pk>/', CourseDetailView.as_view(), name='course_detail'),
]
