from rest_framework import serializers
from .models import *
from knox import views as knox_views
from django.contrib.auth import authenticate
from django.contrib.auth.models import User

from django.contrib.auth.hashers import make_password

# class UserSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = CustomUser
#         fields = ['id','username','email']


# class RegisterSerializer(serializers.ModelSerializer):
#     class Meta:
#         model =CustomUser
#         fields = ['id','username','email','password']
#         extra_kwargs = {'password':{'write_only':True}}
#     def create(self, validated_data):
#         # user = User.objects.create(validated_data['username','email','password'])
#         # return user
#         return super().create(validated_data)

# class RegistrationSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = CustomUser
#         fields = [ 'id','username','email', 'password']
#         extra_kwargs = {'password': {'write_only': True}}

#     def create(self, validated_data):
#         user = CustomUser(
#             username=validated_data['username'],
#             email=validated_data['email']
#         )
#         user.set_password(validated_data['password'])
#         user.save()
#         return user




# class RegistrationSerializer(serializers.ModelSerializer):
#     password = serializers.CharField(write_only=True)

#     class Meta:
#         model = CustomUser
#         fields = ['username','email', 'password' ]

#     def create(self, validated_data):
#         # password = validated_data.pop('password')
#         user = CustomUser(**validated_data)
#         user.password = make_password(validated_data['password'])  # Hash the password
#         user.save()
#         return user





# class CreateUserSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Employee
#         fields = '__all__'

#         # To make a specific field as required field
#         extra_kwargs = { 
#             'EmpId':{'required':True},
#             'password':{'required':True}
#             }

#     def validate(self, attrs):
#         email= attrs.get('email','').strip().lower()
#         emp_id = attrs.get('empId', '') 
#         if Employee.objects.filter(email = email).exists():
#             raise serializers.ValidationError('User with this email is already exists')
#         if Employee.objects.filter(empId=emp_id).exists():
#             raise serializers.ValidationError('Employee with this Emp_id is already exists')
#         return attrs

#     def create(self, validated_data):
#         user = Employee.objects.create(**validated_data)
#         return user

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = '__all__'



class UpdateUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = '__all__'
    
    def update(self, instance, validated_data):
        password = validated_data.pop('EmpId',None)
        # if password:
        #     instance.set_password('EmpId')
        instance = super().update(instance, validated_data)
        instance.save()
        return instance
    
# class LoginSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Employee
#         fields = ['email','password']
#         # email = serializers.EmailField()
#         # password = serializers.CharField(style ={'input_type':'password'},trim_whitespace = False)

#     def validate(self, attrs):
#         email = attrs.get('email').lower()
#         password = attrs.get('password')

#         if not email or not password:
#             raise serializers.ValidationError({'error':'Please give both email and password '})
#         if not Employee.objects.filter(email = email).exists():
#             raise serializers.ValidationError('email doesnot exist')
#         user =authenticate(request=self.context.get('request',email = email, password = password))  
#         if not user:
#                 raise serializers.ValidationError("wrong credentials")
#         attrs['user'] = user
#         return attrs
    
# class LoginSerializer(serializers.Serializer):
#     email = serializers.CharField()
#     password = serializers.CharField(write_only=True)

#     def validate(self, data):
#         user = None
#         email = data.get('email')
#         password = data.get('password')

#         if email and password:
#             user = authenticate(email=email, password=password)

#         if not user:
#             raise serializers.ValidationError('Incorrect credentials')

#         data['user'] = user
#         return data
    


# from knox.models import AuthToken
# from rest_framework import serializers

# class LoginSerializer(serializers.Serializer):
#     email = serializers.EmailField()
#     password = serializers.CharField()

#     def validate(self, data):
#         user = None
#         email = data.get('email')
#         password = data.get('password')

#         if email and password:
#             user = authenticate(username=email, password=password)

#         if not user:
#             raise serializers.ValidationError('Incorrect email or password')

#         data['user'] = user
#         return data
# class LoginSerializer(serializers.ModelSerializer):
#     class Meta:
#         model =CustomUser
#         fields = [ 'email', 'password']
#         extra_kwargs = {'password': {'write_only': True}}

#     def create(self, validated_data):
#         user = CustomUser(
#             username=validated_data['user'],
#             email=validated_data['email']
#         )
#         user.set_password(validated_data['password'])
#         user.save()
#         return user