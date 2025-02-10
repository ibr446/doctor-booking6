from django.urls import path
from .views import (DoctorApiView, NewsApiView,
                    DoctorFilterView, RegisterApiView, LoginApiView, DoctorUpdateApiView, UserUpdateView, BookingAPIView, DoctorDateAPIView)

urlpatterns = [
    path("register/", RegisterApiView.as_view(), name="register"),
    path("login/", LoginApiView.as_view(), name="login"),
    path('doctor', DoctorApiView.as_view(), name='doctor-list'),
    path("doctors/update/<int:pk>/", DoctorUpdateApiView.as_view(), name="doctors-update"),
    path('date/', DoctorDateAPIView.as_view(),name='date-list'),
    path("booking/<int:pk>/", BookingAPIView.as_view(), name="booking"),
    path("users/update/<int:pk>/", UserUpdateView.as_view(), name="users"),
    path('doctor/<int:pk>', DoctorApiView.as_view(), name='doctors-detail'),
    path("search", DoctorFilterView.as_view(), name='search'),
    path('news/', NewsApiView.as_view(), name='news-list'),
    path('news/<int:pk>', NewsApiView.as_view(), name='news-detail')
]





