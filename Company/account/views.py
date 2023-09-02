from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from rest_framework.generics import CreateAPIView,UpdateAPIView, DestroyAPIView,ListAPIView
from rest_framework.permissions import AllowAny
from .models import *
from . serializers import *
from django.contrib.auth import login
from knox.models import AuthToken
from rest_framework import generics, permissions

# Create your views here.
# class RegisterAPI(generics.GenericAPIView):
#     serializer_class = RegisterSerializer
#     def post(self, request, *args, **kwargs):
#         serializer = self.get_serializer(data = request.data)
#         serializer.is_valid(raise_exception = True)
#         user = serializer.save()
#         return Response({"user": serializer.data,
#                          "token": AuthToken.objects.create(user)[1]
#                          })

# class RegisterUserAPI(APIView):
#     # serializer_class = RegistrationSerializer
#     # def post(self, request, *args, **kwargs):
#     #     serializer = self.get_serializer(data = request.data)
#     #     serializer.is_valid(raise_exception = True)
#     #     user = serializer.save()
#     #     return Response({"user": serializer.data,
#     #                      "token": AuthToken.objects.create(user)[1]
#     #                      })
#     def post(self, request):
#         serializer = RegisterSerializer(data=request.data)
#         if serializer.is_valid():
#             user = serializer.save()
#             token = AuthToken.objects.create(user=user)  # Create a token for the user
#             response_data = {
#                 "message": "User registered successfully",
#                 "token": token[1],  # Get the token key from the result tuple
#             }
#             return Response(response_data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# create a new user
# class CreateUserAPI(CreateAPIView):
#     queryset = Employee.objects.all()
#     serializer_class = CreateUserSerializer
#     permission_classes = (AllowAny,)

# list all employees
class ListUserAPIView(ListAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

# update employee details
class UpdateUserAPI(UpdateAPIView):
    queryset = Employee.objects.all()
    serializer_class = UpdateUserSerializer

# delete a particular employee
class DeleteUserAPIView(DestroyAPIView):
    queryset = Employee.objects.all()
    lookup_field = 'pk'  # The field to use for deleting the object, e.g., 'id' or 'Emp_id
   


#######         login API
# class LoginAPIView(knox_views.LoginView):
#     permission_classes = (AllowAny,)
#     serializer_class = LoginSerializer

#     # def post(self, request, format = None):
#     #     serializer = self.serializer_class(data = request.data)
#     #     if serializer.is_valid(raise_exception=True):
#     #         user = serializer.validated_data['user']
#     #         login(request, user)
#     #         response = super().post(request, format=None)
#     #     else:
#     #         return Response({'errors':serializer.errors}, status= status.HTTP_400_BAD_REQUEST)
#     #     return Response(response.data,status=status.HTTP_200_OK)

#     def post(self, request, format=None):
#         serializer = LoginSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         user = serializer.validated_data['user']
#         _, token = AuthToken.objects.create(user)
#         return Response({"user_id": user.id, "token": token}, status=status.HTTP_200_OK)



# from django.contrib.auth import login
# from rest_framework import permissions
# from rest_framework.authtoken.serializers import AuthTokenSerializer
# from knox.views import LoginView as knoxLoginView

# class LoginAPIView(knoxLoginView):
#     permission_classes = (permissions.AllowAny,)

#     def post(self, request, format = None):
#         serializer = AuthTokenSerializer(data = request.data)
#         serializer.is_valid(raise_exception=True)
#         user = serializer.validated_data['user']
#         login(request, user)
#         return super(LoginAPIView,self).post(request, format=None)






