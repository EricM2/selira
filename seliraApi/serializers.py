from rest_framework import serializers

from .models import Hero
from .entities.nodes import Ecommerce, Client, Transporter, Order
import uuid

class HeroSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Hero
        fields = ('name', 'alias')

class OrderSerializer(serializers.Serializer):
    orderId= serializers.UUIDField()
    clientName = serializers.CharField(max_length=200)
    clientAdress = serializers.CharField(max_length=200)
    description = serializers.CharField(max_length=500)
    clientPhoneNumber = serializers.CharField(max_length=200)
    clientEmail = serializers.EmailField()
    estimatedDeliveryTime = serializers.CharField()
    def create(self, validated_data):
        """
        Create and return a new `Snippet` instance, given the validated data.
        """
        order = Order(
            orderId= validated_data['orderId'],
            clientName = validated_data['clientName'],
            clientAdress= validated_data['clientAdress'],
            description= validated_data['description'],
            clientPhoneNumber= validated_data['clientPhoneNumber'],
            clientEmail= validated_data['clientEmail'],
            estimatedDeliveryTime= validated_data['estimatedDeliveryTime']
        )
        order.save()
        return order


class EcommerceSerializer(serializers.Serializer):
    commerceId = serializers.UUIDField()
    commerceName = serializers.CharField(max_length=200)
    commerceURL =  serializers.URLField()
    commerceEmail = serializers.EmailField()
    commerceAdress = serializers.CharField(max_length=200)
    commercePhone = serializers.CharField(max_length=200)
    commerceDescription = serializers.CharField(max_length=500)
    commerceDateJoined = serializers.CharField(max_length=200)
    commerceDateLeaved = serializers.CharField(max_length=200)
    def create(self, validated_data):
        """
        Create and return a new `Snippet` instance, given the validated data.
        """
        ecommerce=Ecommerce(commerceId= validated_data['commerceId'],
                         commerceName= validated_data['commerceName'],
                         commerceURL= validated_data['commerceURL'],
                         commerceEmail= validated_data['commerceEmail'],
                         commerceAdress= validated_data['commerceAdress'],
                         commercePhone= validated_data['commercePhone'],
                         commerceDescription= validated_data['commerceDescription'],
                         commerceDateJoined= validated_data['commerceDateJoined'],
                         commerceDateLeaved= validated_data['commerceDateLeaved']
                        )
        ecommerce.save()
        return ecommerce
    def update(self, instance, validated_data):
        """
        Update and return an existing `Snippet` instance, given the validated data.
        """
        instance.commerceId = validated_data.get('commerceId', instance.commerceId)
        instance.commerceName = validated_data.get('commerceName', instance.commerceName)
        instance.commerceURL = validated_data.get('commerceURL', instance.commerceURL)
        instance.commerceEmail = validated_data.get('commerceEmail', instance.commerceEmail)
        instance.commerceAdress = validated_data.get('commerceAdress', instance.commerceAdress)
        instance.commercePhone = validated_data.get('commercePhone', instance.commercePhone)
        instance.commerceDescription = validated_data.get('commerceDescription', instance.commerceDescription)
        instance.commerceDateJoined = validated_data.get('commerceDateJoined', instance.commerceDateJoined)
        instance.commerceDateLeaved = validated_data.get('commerceDateLeaved', instance.commerceDateLeaved)
        instance.save()
        return instance

class TransporterSerializer(serializers.Serializer):
    transporterId = serializers.UUIDField()
    transporterName = serializers.CharField(max_length=200)
    transporterEmail = serializers.EmailField()
    transporterAdress = serializers.CharField(max_length=200)
    transporterPhone = serializers.CharField(max_length=200)
    transporterNumId= serializers.CharField(max_length=200)
    transporterVehicule = serializers.CharField(max_length=200)
    transporterLong =  serializers.FloatField()
    transporterLat =  serializers.FloatField()
    transporterDateJoined = serializers.CharField(max_length=200)
    transporterDateLeaved = serializers.CharField(max_length=200)
    def create(self, validated_data):
        """
        Create and return a new `Snippet` instance, given the validated data.
        """
        transporter= Transporter(transporterId= validated_data['transporterId'],
                            transporterName= validated_data['transporterName'],
                            transporterEmail= validated_data['transporterEmail'],
                            transporterAdress= validated_data['transporterAdress'],
                            transporterPhone= validated_data['transporterPhone'],
                            transporterNumId= validated_data['transporterNumId'],
                            transporterVehicule= validated_data['transporterVehicule'],
                            transporterLong= validated_data['transporterLong'],
                            transporterLat= validated_data['transporterLat'],
                            transporterDateJoined= validated_data['transporterDateJoined'],
                            transporterDateLeaved= validated_data['transporterDateLeaved']
                        )
        transporter.save()
        return transporter


class ClientSerializer(serializers.Serializer):
    clientId = serializers.UUIDField()
    clientName = serializers.CharField(max_length=200)
    clientEmail = serializers.EmailField()
    clientAdress = serializers.CharField(max_length=200)
    clientPhone = serializers.CharField(max_length=200)
    clientDateJoined = serializers.CharField(max_length=200)
    clientDateLeaved = serializers.CharField(max_length=200)
    def create(self, validated_data):
        """
        Create and return a new `Snippet` instance, given the validated data.
        """
        client=Client(clientId= validated_data['clientId'],
                        clientName= validated_data['clientName'],
                        clientEmail= validated_data['clientEmail'],
                        clientAdress= validated_data['clientAdress'],
                        clientPhone= validated_data['clientPhone'],
                        clientDateJoined= validated_data['clientDateJoined'],
                        clientDateLeaved= validated_data['clientDateLeaved']
                        )
        client.save()
        return client

