from rest_framework import serializers
from .models import *


class UserSerializer(serializers.ModelSerializer):
    avatar = serializers.SerializerMethodField(source='avatar')

    def get_avatar(self, obj):
        request = self.context['request']
        if obj.avatar and not obj.avatar.name.startswith("/static"):

            path = '/static/%s' % obj.avatar.name

            return request.build_absolute_uri(path)

    class Meta:
        model = User
        fields = ['id', 'first_name', 'last_name',
                  'username', 'password', 'email',
                  'avatar']
        extra_kwargs = {
            'password': {
                'write_only': True
            }
        }

    def create(self, validated_data):
        data = validated_data.copy()
        user = User(**data)
        user.set_password(user.password)
        user.save()

        return user


class BusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bus
        fields = ['user', 'Busroutes', 'booking_date']


class BusroutesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Busroutes
        fields = ['name', 'point_of_departure', 'destination', 'pricelist']


class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = '__all__'


class Ticket_detailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ticket_details
        fields = '__all__'