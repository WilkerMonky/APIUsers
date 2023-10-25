from django.urls import path, include
from rest_framework.routers import SimpleRouter

from .views import  UsuarioViewSet, LoginView


router = SimpleRouter()
router.register('usuarios', UsuarioViewSet)



# Ou, alternativamente, você pode usar o nome do modelo associado à view, se houver:
# router.register('userlogin', LoginView, basename='user') 

urlpatterns = [
    path('login/', LoginView.as_view(), name= 'login')
]
