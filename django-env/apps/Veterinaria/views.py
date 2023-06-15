
from django.contrib.sessions.models import Session
from rest_framework import status
from rest_framework.response import Response
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from apps.Veterinaria.api.serializer import UserTokenSerializers
from rest_framework.views import APIView
from datetime import datetime

class UserToken(APIView):
    def post(self, request, *args, **kwargs):
        try:
            user_token = Token.objects.get(
                user = UserTokenSerializers().Meta.objects.filter(username = username).first()
            )
            return Response({
                'token': user_token.key
            })
        except:
            return Response({
                'error': 'credenciales enviadas incorrectas.'
            }, status= status.HTTP_400_BAD_REQUEST)
            
class Login(ObtainAuthToken):
    
    def post(self, request, *args, **kwargs):
        print(f'{self=}')
        print(f'{request.data=}')
        login_serializer = self.serializer_class(data = request.data, context={'request':request})
        if login_serializer.is_valid():
            user = login_serializer.validated_data['user']
            if user.is_active:
                token,created = Token.objects.get_or_create(user=user)
                user_serializer = UserTokenSerializers(user)
                if created:
                    return Response({
                        'token': token.key,
                        'user': user_serializer.data ,
                        'message': 'Inicio de sesion exitoso'
                        },status = status.HTTP_201_CREATED)
                else:
                #     
                #     token = Token.objects.create( user = user)
                #     return Response({
                #         'token': token.key,
                #         'user': user,
                #         'message': 'Inicio de sesion exitoso'
                #         },status = status.HTTP_201_CREATED)
                    token.delete()
                    return Response({'error': 'Ya se ha iniciado sesión con este usuario'},status = status.HTTP_409_CONFLICT)
            else:
                return Response({'error': 'este user no puede iniciar sesion'}, status = status.HTTP_401_UNAUTHORIZED)
        else :
            return Response ({'error': 'nombre del user o contraseña incorrecta.'}, status = status.HTTP_400_BAD_REQUEST)
        
class Logout(APIView):
    
    def post(self, request, *args, **kwargs):
        
        try:           
            token = request.POST.get('token')
            token = Token.objects.filter(key = token).first()
            
            if token:
                user = token.user 
                               
                all_sessions = Session.objects.filter(expire_date__gte = datetime.now())
                if all_sessions.exists():
                    for session in all_sessions:
                        session_data = session.get_decoded()
                        if user.id == int(session_data.get('_auth_user_id')):
                                session.delete() 
                                            
                token.delete()        
                    
                session_message = 'Sesiones de usuario eliminadas.'
                token_message = 'Token eliminado.'
                return Response ({'token_message': token_message,'session_message':session_message}, status = status.HTTP_200_OK)
            return Response({'error': 'No se ha encontrado un usuario con estas credenciales.'}, status = status.HTTP_400_BAD_REQUEST)
        
        except:
            
            return Response({'error': 'No se ha encontrado token en la peticion.'}, status = status.HTTP_409_CONFLICT)     

            

        
            
            
        