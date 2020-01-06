from django.contrib.auth import authenticate, get_user_model
from rest_framework import serializers


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        user = authenticate(username=data['username'], password=data['password'])
        if not user:
            raise serializers.ValidationError('Incorrect username or password.')
        if not user.is_active:
            raise serializers.ValidationError('User is disabled.')
        return user


class UserSerializer(serializers.ModelSerializer):
    groups = serializers.SlugRelatedField(
        many=True, read_only=True, slug_field='name'
    )

    class Meta:
        model = get_user_model()
        fields = '__all__'
        read_only_fields = ['staff', 'active', 'admin']
        extra_kwargs = {
            "password": {
                "write_only": True
            },
        }
