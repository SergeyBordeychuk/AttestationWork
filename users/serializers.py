from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from users.models import CustomUser
from users.validators import EmailValidator, PasswordValidator, AgeValidator


class UserSerializer(serializers.ModelSerializer):
    password1 = serializers.CharField(style={'input_type': 'password'}, write_only=True)
    password2 = serializers.CharField(style={'input_type': 'password'}, write_only=True)

    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password1', 'password2', 'birth_day',]
        validators = [EmailValidator(email='email'), PasswordValidator(password='password1'), AgeValidator(birthday='birth_day'),]

    def validate(self, attrs):
        password1 = attrs.get('password1')
        password2 = attrs.get('password2')
        if password1 != password2:
            raise ValidationError('Passwords don\'t match')
        attrs['password'] = password1
        attrs.pop('password1')
        attrs.pop('password2')
        return attrs
