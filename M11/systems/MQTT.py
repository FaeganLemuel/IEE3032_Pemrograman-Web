from rest_framework.generics import RetrieveUpdateDestroyAPIView
from rest_framework.response import Response
import paho.mqtt.client as mqtt
from systems.Machinelearning import air_keju, air_coklat, air_kosong


from .serializers import ActuatorSerializer, SensorSerializer
from .models import Actuator, Sensor


def update_act(self, request, *args, **kwargs):
    tepung_kosong = Sensor.objects.get(name="kot")
    garam_kosong = Sensor.objects.get(name="kog")
    ragi_kosong = Sensor.objects.get(name="kor")
    act_kosong = Actuator.objects.get(name="airko")
    airko = air_kosong(int(tepung_kosong.value), int(garam_kosong.value), int(ragi_kosong.value))
    data = {'value': airko}
    serializer = ActuatorSerializer(act_kosong, data=data, partial=True)
    if serializer.is_valid():
        serializer.save()
        print("updated actuator value to", airko)

    tepung_coklat = Sensor.objects.get(name="kct")
    coklat = Sensor.objects.get(name="kcc")
    ragi_coklat = Sensor.objects.get(name="kcr")
    act_coklat = Actuator.objects.get(name="airco")
    airco = air_coklat(int(tepung_coklat.value), int(coklat.value), int(ragi_coklat.value))
    data = {'value': airco}
    serializer = ActuatorSerializer(act_coklat, data=data, partial=True)
    if serializer.is_valid():
        serializer.save()
        print("updated actuator value to", airco)

    tepung_keju = Sensor.objects.get(name="ket")
    keju = Sensor.objects.get(name="kek")
    ragi_keju = Sensor.objects.get(name="ker")
    act_keju = Actuator.objects.get(name="airke")
    airke = air_keju(int(tepung_keju.value), int(keju.value), int(ragi_keju.value))
    data = {'value': airke}
    serializer = ActuatorSerializer(act_keju, data=data, partial=True)
    if serializer.is_valid():
        serializer.save()
        print("updated actuator value to", airke)
    else :
        print("serializer failed")


def update_kot(client, userdata, msg):
    object_ = Sensor.objects.get(name="kot")
    data = {
        'value': msg.payload.decode('utf-8')
    }
    serializer = SensorSerializer(object_, data=data, partial=True)
    if serializer.is_valid():
        serializer.save()
    print('recieved data ', msg.payload.decode('utf-8'))


def update_kog(client, userdata, msg):
    object_ = Sensor.objects.get(name="kog")
    data = {
        'value': msg.payload.decode('utf-8')
    }
    serializer = SensorSerializer(object_, data=data, partial=True)
    if serializer.is_valid():
        serializer.save()
    print('recieved data ', msg.payload.decode('utf-8'))

def update_kor(client, userdata, msg):
    object_ = Sensor.objects.get(name="kor")
    data = {
        'value': msg.payload.decode('utf-8')
    }
    serializer = SensorSerializer(object_, data=data, partial=True)
    if serializer.is_valid():
        serializer.save()
    print('recieved data ', msg.payload.decode('utf-8'))


def update_kct(client, userdata, msg):
    object_ = Sensor.objects.get(name="kct")
    data = {
        'value': msg.payload.decode('utf-8')
    }
    serializer = SensorSerializer(object_, data=data, partial=True)
    if serializer.is_valid():
        serializer.save()
    print('recieved data ', msg.payload.decode('utf-8'))


def update_kcc(client, userdata, msg):
    object_ = Sensor.objects.get(name="kcc")
    data = {
        'value': msg.payload.decode('utf-8')
    }
    serializer = SensorSerializer(object_, data=data, partial=True)
    if serializer.is_valid():
        serializer.save()
    print('recieved data ', msg.payload.decode('utf-8'))


def update_kcr(client, userdata, msg):
    object_ = Sensor.objects.get(name="kcr")
    data = {
        'value': msg.payload.decode('utf-8')
    }
    serializer = SensorSerializer(object_, data=data, partial=True)
    if serializer.is_valid():
        serializer.save()
    print('recieved data ', msg.payload.decode('utf-8'))


def update_ket(client, userdata, msg):
    object_ = Sensor.objects.get(name="ket")
    data = {
        'value': msg.payload.decode('utf-8')
    }
    serializer = SensorSerializer(object_, data=data, partial=True)
    if serializer.is_valid():
        serializer.save()
    print('recieved data ', msg.payload.decode('utf-8'))


def update_kek(client, userdata, msg):
    object_ = Sensor.objects.get(name="kek")
    data = {
        'value': msg.payload.decode('utf-8')
    }
    serializer = SensorSerializer(object_, data=data, partial=True)
    if serializer.is_valid():
        serializer.save()
    print('recieved data ', msg.payload.decode('utf-8'))


def update_ker(client, userdata, msg):
    object_ = Sensor.objects.get(name="ker")
    data = {
        'value': msg.payload.decode('utf-8')
    }
    serializer = SensorSerializer(object_, data=data, partial=True)
    if serializer.is_valid():
        serializer.save()
    print('recieved data ', msg.payload.decode('utf-8'))


def run_mqtt():
    client = mqtt.Client("DjangoApp")

    client.message_callback_add("roti/kosong/tepung", update_kot)
    client.message_callback_add("roti/kosong/garam", update_kog)
    client.message_callback_add("roti/kosong/ragi", update_kor)

    client.message_callback_add("roti/coklat/tepung", update_kct)
    client.message_callback_add("roti/coklat/coklat", update_kcc)
    client.message_callback_add("roti/coklat/ragi", update_kcr)

    client.message_callback_add("roti/keju/tepung", update_ket)
    client.message_callback_add("roti/keju/keju", update_kek)
    client.message_callback_add("roti/keju/ragi", update_ker)

    client.message_callback_add("roti/keju/ragi", update_act)

    client.connect('localhost', 1883)
    client.loop_start()
    client.subscribe("roti/kosong/tepung")
    client.subscribe("roti/kosong/garam")
    client.subscribe("roti/kosong/ragi")

    client.subscribe("roti/coklat/tepung")
    client.subscribe("roti/coklat/coklat")
    client.subscribe("roti/coklat/ragi")

    client.subscribe("roti/keju/tepung")
    client.subscribe("roti/keju/keju")
    client.subscribe("roti/keju/ragi")
