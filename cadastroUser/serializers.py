from rest_framework import serializers
from .models import UsuarioComum


class UsuarioComumSerializer(serializers.ModelSerializer):
   
   
    class Meta:
        model = UsuarioComum
        #passando kwargs para não retornarem dados sensiveis como email e senha, quando as requisições forem feitas
        extra_kwargs = {
            'email':{'write_only': True},
            #'password':{'write_only':True}
          }
        fields = (
            'username',
            'password',
            'first_name',
            'last_name',
            'email',
            'is_staff',
            'date_joined',
            'data_nasc',
            'endereco',
            'criacao',
            'atualizacao',
        )
        read_only_fields = ('is_staff','criacao','atualizacao', 'date_joined')
    


    #Cria Um novo usuário usando os recursos de autenticação e segurança do django
    def create(self, validated_data):
        user = UsuarioComum(**validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)