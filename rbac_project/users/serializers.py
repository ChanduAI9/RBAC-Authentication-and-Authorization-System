from rest_framework import serializers
from .models import Role,User

class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model= Role
        fields='__all__'

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password', 'role']
        extra_kwargs = {
            'password': {'write_only': True},  # Prevent password from being exposed
        }

    def create(self, validated_data):
        # Hash the password when creating a new user
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password'],
            role=validated_data.get('role')
        )
        return user    
