from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from foundation.models import Instrument, Sensor, TimeSeriesDatum


class InstrumentSerializer(serializers.Serializer):


    id = serializers.IntegerField(read_only=True)
    location = serializers.CharField(validators=[
        UniqueValidator(queryset=Instrument.objects.all())
    ])
    serial_number = serializers.UUIDField(read_only=True)
    name = serializers.CharField(read_only=True)

    def create(self, validated_data):

        location = validated_data.get('location', None)
        instrument = Instrument.objects.create(location=location)
        return instrument


    def update(self, object, validated_data):

        object.url = validated_data.get('url')
        object.save()
        return object
