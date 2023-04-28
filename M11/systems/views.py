from django.shortcuts import render, HttpResponse
from systems.models import Sensor, Actuator
from django.template import loader
from systems.MQTT import run_mqtt
import sqlite3


def main_page(request):
    sensor = Sensor.objects.all().values()
    actuator = Actuator.objects.all().values()
    template = loader.get_template('details.html')
    context = {
        'sensors': sensor,
        'actuators': actuator,
    }
    return HttpResponse(template.render(context, request))


run_mqtt()
