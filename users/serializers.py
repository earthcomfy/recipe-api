from rest_framework import serializers
from django.contrib.auth import authenticate
from django.contrib.auth.password_validation import validate_password

from .models import CustomUser, Profile


class CustomUserSerializer(serializers.ModelSerializer):
    """
    Serializer class to seralize CustomUser model.
    """
    class Meta:
        model = CustomUser
        fields = ('id', 'username', 'email')


class UserRegisterationSerializer(serializers.ModelSerializer):
    """
    Serializer class to serialize registeration requests and create a new user.
    """
    class Meta:
        model = CustomUser
        fields = ('id', 'username', 'email', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        return CustomUser.objects.create_user(**validated_data)


class UserLoginSerializer(serializers.Serializer):
    """
    Serializer class to authenticate users with email and password.
    """
    email = serializers.CharField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        user = authenticate(**data)
        if user and user.is_active:
            return user
        raise serializers.ValidationError('Incorrect Credentials')


class ProfileSerializer(CustomUserSerializer):
    """
    Serializer class to serializer the user Profile model
    """
    class Meta:
        model = Profile
        fields = ('favorites',)


class PasswordChangeSerializer(serializers.Serializer):
    """
    Serializer class for changing user password
    """
    old_password = serializers.CharField(write_only=True, required=True)
    new_password = serializers.CharField(write_only=True, required=True)

    def validate_old_password(self, value):
        user = self.context['request'].user
        if not user.check_password(value):
            raise serializers.ValidationError("Old password is not correct")
        return value

    def validate_new_password(self, value):
        validate_password(value)
        return value

    def update(self, instance, validated_data):
        instance.set_password(validated_data['new_password'])
        instance.save()
        return instance
