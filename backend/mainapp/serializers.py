from rest_framework.serializers import ModelSerializer
from mainapp.models import MenuItem


class MenuSerializer(ModelSerializer):
    class Meta:
        model = MenuItem
        fields = '__all__'
