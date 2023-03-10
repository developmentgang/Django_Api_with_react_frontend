from rest_framework.serializers import ModelSerializer
from django.contrib.auth.models import User


class UserSerilizer(ModelSerializer):
    class Meta:
        model = User
        fields = ['id']

        
class CustomUserSerilizer(ModelSerializer):
    class Meta:
        model = User
        fields ='__all__'
        # fields = ['username','first_name','last_name']