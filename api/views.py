from datetime import timedelta

from django.core.serializers import serialize
from django.utils.timezone import now
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from .models import Doctor, News, User, Date
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.throttling import AnonRateThrottle, UserRateThrottle
from django.contrib.auth.hashers import check_password, make_password
from .serializers import (DoctorSerializer, NewsSerializer, RegisterSerializer,
                          DoctorUpdateSerializer, LoginSerializer, UserUpdateSerializer, DoctorDateSerializer, BookingSerializer)
from rest_framework import filters, generics
from rest_framework.filters import SearchFilter
from drf_spectacular.utils import extend_schema, OpenApiParameter
from rest_framework.permissions import IsAuthenticated
from rest_framework.parsers import MultiPartParser, FormParser






class RegisterApiView(APIView):
    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save(password=make_password(serializer.validated_data['password']))
            refresh = RefreshToken.for_user(user)
            access_token = str(refresh.access_token)
            return Response({
                    "refresh": str(refresh),
                    "access": access_token,
                    "user": serializer.data
                },status=status.HTTP_201_CREATED
            )
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class LoginApiView(APIView):
    @extend_schema(
        summary="User Login",
        description="Login using email and password to obtain JWT tokens.",
        request=LoginSerializer,  # Specify request body fields
        responses={
            200: OpenApiParameter(name="Tokens", description="JWT access and refresh tokens"),
            400: OpenApiParameter(name="Errors", description="Invalid credentials or validation errors"),
        },
        tags=["User Authentication"]
    )
    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            email = serializer.validated_data.get('email')
            password = serializer.validated_data.get('password')

            user = User.objects.get(email=email)
            if user.check_password(password):
                if not user.is_active:
                    return Response({"detail": "User account is inactive."}, status=status.HTTP_400_BAD_REQUEST)

                refresh = RefreshToken.for_user(user)
                access_token = str(refresh.access_token)

                return Response({
                    "refresh": str(refresh),
                    "access": access_token,
                }, status=status.HTTP_200_OK)
        else:
            return Response({"detail": "Invalid password or email"}, status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class UserUpdateView(APIView):
    parser_classes = (MultiPartParser, FormParser)

    @extend_schema(
        request=UserUpdateSerializer,
        responses={200: "User updated successfully"}
    )
    def put(self, request, pk):
        user = get_object_or_404(User, pk=pk)  # Gracefully handle non-existing user
        serializer = UserUpdateSerializer(instance=user, data=request.data, partial=False)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "User updated successfully"}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class DoctorApiView(APIView):
    permission_classes = [IsAuthenticated]
    throttle_classes = (AnonRateThrottle, UserRateThrottle)

    def get(self, requests, pk=None):
        if pk:
            try:
                doctor = Doctor.objects.get(pk=pk)
                serializer = DoctorSerializer(doctor)
                return Response(serializer.data)
            except:
                return Response({'error': 'Doctor not found'}, status=status.HTTP_404_NOT_FOUND)
        else:
            doctor = Doctor.objects.all()
            serializer = DoctorSerializer(doctor, many=True)
            return Response(serializer.data)




class DoctorUpdateApiView(APIView):
    permission_classes = (IsAuthenticated,)

    @extend_schema(
        summary="Doctor Update",
        description="Doctor update data",
        request=DoctorUpdateSerializer,  # Specify request body fields
        responses={
            200: OpenApiParameter(name="Update", description="Doctor update data"),
            400: OpenApiParameter(name="Errors", description="Invalid credentials or validation errors"),
        },
        tags=["Doctor Update"]
    )
    def put(self, request, pk):
        doctor = get_object_or_404(Doctor, pk=pk)
        serializer = DoctorUpdateSerializer(doctor, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




class DoctorFilterView(ListAPIView):
    serializer_class = DoctorSerializer
    queryset = Doctor.objects.all()
    filter_backends = [DjangoFilterBackend, SearchFilter]
    search_fields = ['location', 'clinic_name']
    filterset_fields = ['experience', 'rating_percentage', 'consultation_fee', 'location']



class NewsApiView(APIView):
    def get(self, requests, pk=None):
        if pk:
            try:
                news = News.objects.get(pk=pk)
                serializer = NewsSerializer(news)
                return Response(serializer.data)
            except:
                return Response({'error': 'News not found'}, status=status.HTTP_404_NOT_FOUND)
        else:
            news = News.objects.all()
            serializer = NewsSerializer(news, many=True)
            return Response(serializer.data)



class DoctorDateAPIView(APIView):
    def get(self, request):
        date = Date.objects.all()
        serializer = DoctorDateSerializer(date, many=True)
        return Response(serializer.data)



class BookingAPIView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, pk):
        user = request.user
        Date.objects.filter(pk=pk, status='pending').update(user=user, status='confirmed')
        try:
            date = Date.objects.get(pk=pk, status='confirmed')
        except Date.DoesNotExist:
            return Response({"error": "Date not found or not pending"}, status=404)

        serializer = BookingSerializer(date)
        return Response(serializer.data)









