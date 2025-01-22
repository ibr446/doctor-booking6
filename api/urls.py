from django.urls import path
from .views import DoctorApiView, NewsApiView

urlpatterns = [
    path('doctor', DoctorApiView.as_view(), name='doctor-list'),
    path('doctor/<int:pk>', DoctorApiView.as_view(), name='doctors-detail'),
    path('news/', NewsApiView.as_view(), name='news-list'),
    path('news/<int:pk>', NewsApiView.as_view(), name='news-detail')
]
