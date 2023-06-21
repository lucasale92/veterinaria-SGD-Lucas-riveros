from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.response import Response
from rest_framework import viewsets
from apps.Veterinaria.api.serializer.serializer import ClienteSerializer, ClienteListSerializer, UpdateClienteSerializer
from apps.Veterinaria.models import Cliente

class UserViewSet(viewsets.GenericViewSet):
    model = Cliente
    serializer_class = ClienteSerializer
    list_serializer_class = ClienteListSerializer
    queryset = Cliente.objects.filter(estado=True)

    def get_object(self, pk):
        return get_object_or_404(self.model, pk=pk)

    def get_queryset(self):
        if self.queryset is None:
            self.queryset = self.model.objects.filter(estado=True).values('id', 'nombre')
        return self.queryset

    def list(self, request):
        """
        Informacion sobre la lista de clientes 
        """
        users = self.get_queryset()
        users_serializer = self.list_serializer_class(users, many=True)
        return Response(users_serializer.data, status=status.HTTP_200_OK)
    
    def create(self, request):
        """
        Aqui se crean lo clientes
        """
        user_serializer = self.serializer_class(data=request.data)
        if user_serializer.is_valid():
            user_serializer.save()
            return Response({
                'message': 'Usuario registrado correctamente.'
            }, status=status.HTTP_201_CREATED)
        return Response({
            'message': 'Hay errores en el registro',
            'errors': user_serializer.errors
        }, status=status.HTTP_400_BAD_REQUEST)    
        
    def retrieve(self, request, pk=None):
        """
        Aqui se buscan por N° de ID
        """
        user = self.get_object(pk)
        user_serializer = self.serializer_class(user)
        return Response(user_serializer.data)

    def update(self, request, pk=None):
        """
        Aqui se actualiza la informacion
        """
        user = self.get_object(pk)
        user_serializer = UpdateClienteSerializer(user, data=request.data)
        if user_serializer.is_valid():
            user_serializer.save()
            return Response({
                'message': 'Usuario actualizado correctamente'
            }, status=status.HTTP_200_OK)
        return Response({
            'message': 'Hay errores en la actualización',
            'errors': user_serializer.errors
        }, status=status.HTTP_400_BAD_REQUEST)
        
    def destroy(self, request, pk=None):
        """
        Aqui se elimina el usuario 
        """
        user_destroy = self.model.objects.filter(id=pk).update(estado=False)
        if user_destroy == 1:
            return Response({
                'message': 'Usuario eliminado correctamente'
            })
        return Response({
            'message': 'No existe el usuario que desea eliminar'
        }, status=status.HTTP_404_NOT_FOUND)
