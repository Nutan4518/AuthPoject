# from re import T
from django.db.models import fields
from rest_framework import serializers
from .models import *


class UserSerializer(serializers.ModelSerializer):
    # media_segment_id = serializers.CharField(max_length= 50,default = "all")

    class Meta:
        model = User
        fields = ('email',
                  'name',
                  'phone',
                  'emp_code',
                  )

    def create(self, validated_data):
        user = User(email=validated_data['email'],
                    name=validated_data['name'],
                    phone=validated_data['phone'],
                    emp_code=validated_data['emp_code'],
                    # current_status=1,
                    # is_active=1

                    )
        user.set_password(validated_data['password'])
        user.save()
        return user

class LoginSerializer(serializers.Serializer):
    email = serializers.CharField()
    password = serializers.CharField()



