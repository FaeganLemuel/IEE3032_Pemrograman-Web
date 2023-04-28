from rest_framework import serializers

from .models import Actuator, Sensor


class ActuatorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actuator

        fields = "__all__"


class SensorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sensor

        fields = "__all__"
