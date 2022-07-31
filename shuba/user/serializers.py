from rest_framework import serializers
# from .models import User
from django.contrib.auth import authenticate, models
from django.contrib.auth.models import User
from user.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            "id",
            "email",
            "is_active",
            "is_superuser",
        ]


class RegistrationSerializer(UserSerializer):
    password = serializers.CharField(
        max_length=128,
        min_length=8,
        write_only=True
    )
    password_submit = serializers.CharField(
        max_length=128,
        min_length=8,
        write_only=True
    )

    class Meta(UserSerializer.Meta):
        fields = UserSerializer.Meta.fields + [
            "password",
            "password_submit",
        ]

    def validate(self, attrs):
        if attrs["password"] != attrs["password_submit"]:
            raise serializers.ValidationError("Passwords unmatched")
        return super().validate(attrs)

    def create(self, validated_data):
        validated_data.pop("password_submit")
        user = User.objects.create_user(**validated_data )
        user.send_register_mail()
        return user


