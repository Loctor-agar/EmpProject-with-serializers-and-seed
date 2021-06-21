from rest_framework import serializers

from .models import Employee, Position


class PositionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Position
        fields = '__all__'


class EmpSerializer(serializers.ModelSerializer):
    position = PositionSerializer()

    class Meta:
        model = Employee
        fields = '__all__'



