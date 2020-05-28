from rest_framework import serializers

from .models import Place, JobRequest


class JobRequestSerializer(serializers.Serializer):
    place = serializers.IntegerField()
    serviceprovider_from = serializers.IntegerField()

    def update(self, instance, validated_data):
        instance.place = validated_data.get('place', instance.place)
        instance.serviceprovider_from = validated_data.get('serviceprovider_from',
                                                           instance.serviceprovider_from)

        return instance

    def create(self, validated_data):
        return JobRequest.objects.create(**validated_data)


class PlaceSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    serviceprovider_owner_id = serializers.IntegerField()
    street = serializers.CharField(max_length=30)
    streetnumber = serializers.IntegerField()
    apnumber = serializers.IntegerField()
    city = serializers.CharField(max_length=30)
    state = serializers.CharField(max_length=30)
    country = serializers.CharField(max_length=30)
    businessname = serializers.CharField(max_length=30)
    phonenumber = serializers.CharField(max_length=30)
    email = serializers.CharField(max_length=30)

    def update(self, instance, validated_data):
        instance.id = validated_data.get('id', instance.id)
        instance.serviceprovider_owner_id = validated_data.get('serviceprovider_owner_id',
                                                               instance.serviceprovider_owner_id)
        instance.street = validated_data.get('street', instance.street)
        instance.streetnumber = validated_data.get('streetnumber', instance.streetnumber)
        instance.apnumber = validated_data.get('apnumber', instance.apnumber)
        instance.city = validated_data.get('city', instance.city)
        instance.state = validated_data.get('state', instance.state)
        instance.country = validated_data.get('country', instance.country)
        instance.businessname = validated_data.get('businessname', instance.businessname)
        instance.phonenumber = validated_data.get('phonenumber', instance.phonenumber)
        instance.email = validated_data.get('email', instance.email)
        return instance

    def create(self, validated_data):
        return Place.objects.create(**validated_data)
