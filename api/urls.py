from django.urls import path
from .views import DoctorApiView, NewsApiView, DoctorFilterView, RegisterApiView

urlpatterns = [
    path("register/", RegisterApiView.as_view(), name="register"),
    path('doctor', DoctorApiView.as_view(), name='doctor-list'),
    path('doctor/<int:pk>', DoctorApiView.as_view(), name='doctors-detail'),
    path("search", DoctorFilterView.as_view(), name='search'),
    path('news/', NewsApiView.as_view(), name='news-list'),
    path('news/<int:pk>', NewsApiView.as_view(), name='news-detail')
]



s