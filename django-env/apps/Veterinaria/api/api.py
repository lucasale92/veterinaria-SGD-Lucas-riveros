from rest_framework.response import Response
from rest_framework.views import APIView
from apps.Veterinaria.api.serializer import ClienteSerializer
from rest_framework.decorators import api_view
from apps.Veterinaria.models import Cliente
from rest_framework import status
from apps.Veterinaria.authentication_mixins import Authentication

@api_view(['GET', 'POST'])
def cliente_api_view(request):
    # list
    if request.method == 'GET':
        # queryset
        cliente = Cliente.objects.all()
        cliente_serializer = ClienteSerializer(cliente,many = True)        
        return Response(cliente_serializer.data, status = status.HTTP_200_OK)
    
    # create
    elif request.method == 'POST':
        cliente_serializer = ClienteSerializer(data=request.data)
    
    # validation
        if cliente_serializer.is_valid():
            cliente_serializer.save()
            return Response({'Message':'Usuario Creado correctamente!!'}, status = status.HTTP_201_CREATED)
        return Response(cliente_serializer.errors, status = status.HTTP_400_BAD_REQUEST)
            
@api_view (['GET', 'PUT','DELETE'])
def cliente_detail_api_view(request,pk=None):
    # queryset
    cliente = Cliente.objects.filter(id = pk).first()
    # validation
    if cliente:
    
        # retrieve
        if request.method == 'GET':
            cliente_serializer = ClienteSerializer(cliente)
            return Response(cliente_serializer.data, status = status.HTTP_200_OK)
        
        # update
        elif request.method == 'PUT':
            cliente_serializer = ClienteSerializer(cliente, data=request.data)
            if cliente_serializer.is_valid():
                cliente_serializer.save()
                return Response(cliente_serializer.data, status = status.HTTP_200_OK)
            return Response(cliente_serializer.errors, status = status.HTTP_400_BAD_REQUEST)

        # delete
        elif request.method == 'DELETE':
            cliente.delete()
            return Response({'Message':'Usuario Eliminado correctamente!!'}, status = status.HTTP_200_OK)  

    return Response({'Message':'No se encontro un usuario con los datos proporcionados'}, status = status.HTTP_400_BAD_REQUEST)  