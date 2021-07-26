from rest_framework import serializers
from rest_auth.registration.serializers import RegisterSerializer
from allauth.account.adapter import get_adapter
from rest_framework.authtoken.models import Token

from users.models import MyUser


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = MyUser
        fields = ['id', 'email', 'first_name', 'last_name', 'password',]



class CustomRegisterSerializer(RegisterSerializer):

    first_name = serializers.CharField(max_length=50)
    last_name = serializers.CharField(max_length=50)

    class Meta:
        model = MyUser
        fields = ['email', 'first_name', 'last_name', 'password',]

    def get_cleaned_data(self):
        return {
            'email': self.validated_data.get('email', ''),
            'first_name': self.validated_data.get('first_name', ''),
            'last_name': self.validated_data.get('last_name', ''),
            'password1': self.validated_data.get('password1', ''),
            'password2': self.validated_data.get('password2', ''),
        }

    def save(self, request):
        
        adapter = get_adapter()
        user = adapter.new_user(request)
        self.cleaned_data = self.get_cleaned_data()
        user.first_name = self.cleaned_data.get('first_name')
        user.last_name = self.cleaned_data.get('last_name')
        user.save() 
        adapter.save_user(request, user, self)
        return user


class TokenSerializer(serializers.ModelSerializer):

    class Meta:
        model = Token
        fields = ('key', 'user',)