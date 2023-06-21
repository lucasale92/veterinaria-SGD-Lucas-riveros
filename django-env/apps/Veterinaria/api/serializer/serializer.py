from rest_framework import serializers
from apps.Veterinaria.models import Cliente
from django.contrib.auth.models import User

class UserTokenSerializers(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'nombre', 'apellido')
        
class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = '__all__'
        
    def create(self, validated_data):
        user = Cliente(**validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user
    
class UpdateClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'nombre', 'apellido')

class ClienteListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        
    def to_representation(self, instance):
        return {
            'id': instance.id,
            'username': instance.username,
            'password': instance.password,
    }

       

        