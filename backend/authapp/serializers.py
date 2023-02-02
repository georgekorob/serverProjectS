from rest_framework.serializers import ModelSerializer
from authapp.models import User


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'id', 'is_superuser', 'first_name', 'last_name', 'birth', 'about', 'gender']


class UserInfoSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'is_superuser']
