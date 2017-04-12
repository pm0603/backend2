from django.contrib.auth import get_user_model
from rest_framework import serializers


class PasswordChangeSerializer(serializers.Serializer):
    password = serializers.CharField(max_length=128)


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ('email','username')
