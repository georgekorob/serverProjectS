from rest_framework.serializers import ModelSerializer
from houseapp.models import Nodemcu, PartString


class NodemcuSerializer(ModelSerializer):
    class Meta:
        model = Nodemcu
        fields = '__all__'


class PartStringSerializer(ModelSerializer):
    class Meta:
        model = PartString
        fields = '__all__'
