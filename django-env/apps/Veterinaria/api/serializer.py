from rest_framework import serializers
from apps.Veterinaria.models import Cliente
from django.contrib.auth.models import User

class UserTokenSerializers(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name')
        
        
class ClienteTokenSerializer (serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = ('nombre', 'apellido')
         
class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = '__all__'
        
    # def create(self, validated_data):
    #     user = Cliente(**validated_data)
    #     user.set_password(validated_data['password'])
    #     user.save()
    #     return user
    
    # def update(self, instance, validated_data):
    #     updated_user = super().update(instance, validated_data)
    #     updated_user.set_password(validated_data['password'])
    #     updated_user.save()
    #     return updated_user

class ClienteListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        
    def to_representation(self, instance):
        return{
            'id': instance['id'],
            'username': instance['username'],
            'password': instance['password'],
        }
        
        
    

       

        