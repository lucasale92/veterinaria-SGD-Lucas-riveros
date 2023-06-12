from apps.Veterinaria.authentication import ExpiringTokenAuthentication

class Authentication(object):
    
    def dispatch(self, request, *args, **kwargs):
        
        return super().dispatch(request, *args, **kwargs)