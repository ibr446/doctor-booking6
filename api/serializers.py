from rest_framework import serializers
from .models import Doctor, User, News
from django.conf import settings
from root.settings import BASE_URL


class UserUpdateSerializer(serializers.ModelSerializer):
    avatar = serializers.ImageField()
    class Meta:
        model = User
        fields = ["first_name", "last_name", "avatar"]



class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email', 'password', 'roles')


class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)




class UserSerializer(serializers.ModelSerializer):
    avatar = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'avatar']

    def get_avatar(self, obj):
        if obj.avatar:
            return settings.BASE_URL + obj.avatar.url
        return None



class DoctorSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Doctor
        fields = ['user', 'id', 'specialization', 'experience', 'location', 'clinic_name', 'consultation_fee',
                  'is_consultation_free', 'available_today', 'rating_percentage', 'patient_stories']




class DoctorUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        fields = ['id', 'specialization', 'experience', 'location', 'clinic_name',
                  'consultation_fee', 'is_consultation_free', 'available_today',
                  'rating_percentage', 'patient_stories', ]




class NewsSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    img = serializers.SerializerMethodField()

    class Meta:
        model = News
        fields = ['user','title', 'img', 'created_at']

    def get_img(self, obj):
        if obj.img:
            return settings.BASE_URL + obj.img.url
        return None


