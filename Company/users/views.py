
from rest_framework.permissions import IsAuthenticated
from knox.views import LoginView as KnoxLoginView
from knox.views import LogoutView
from django.shortcuts import render
from rest_framework.views import APIView
from .models import *
from rest_framework import generics
from .serializers import *
from rest_framework.response import Response
from django.contrib.auth import SESSION_KEY, authenticate, login
from datetime import date, datetime
from rest_framework import permissions
from rest_framework import status


class CreateUser(generics.CreateAPIView):
    # permission_classes = [IsAuthenticated]
    serializer_class = UserSerializer

    def post(self, request, format=None):
        result = {}
        # result['status'] = 'NOK'
        # result['valid'] = False
        result["result"] = {'message': 'Unauthorized', 'data': []}
        if request.user.is_authenticated:

            serializer = UserSerializer(data=request.data)
            if serializer.is_valid():

                try:
                    username = serializer.validated_data['email']
                    # password = ''.join(
                    #     random.choices(string.ascii_uppercase + string.ascii_lowercase + string.digits, k=8))
                    password='123456'
                    serializer.validated_data['password'] = password
                    serializer.save()
                    name = request.data['name']
                    email = request.data['email']

                    # if request.data['user_role']=='4':
                    #     obj=User.objects.filter(user_role=4).order_by('-analyst_id')[0]
                    #     obj1=User.objects.last()
                    #     User.objects.filter(id=obj1.id).update(analyst_id=obj.analyst_id+1)

                except:
                    # result['status'] = 'NOK'
                    # result['valid'] = False
                    # result['result']['message'] = "Error in sending mail"
                    return Response(result, status=status.HTTP_422_UNPROCESSABLE_ENTITY)

                # result =dict()
                # result['status'] = 'OK'
                # result['valid'] = True
                result['result']['message'] = "User created successfully !"
                return Response(result, status=status.HTTP_200_OK)
            else:
                result['result']['message'] = (list(serializer.errors.keys())[
                                                   0] + ' - ' + list(serializer.errors.values())[0][0]).capitalize()
                return Response(result, status=status.HTTP_422_UNPROCESSABLE_ENTITY)

        return Response(result, status=status.HTTP_401_UNAUTHORIZED)

class Login(KnoxLoginView):
    permission_classes = (permissions.AllowAny,)
    serializer_class = LoginSerializer

    def post(self, request, format=None):
        serializer = LoginSerializer(data=request.data)
        result = {}
        # result['status'] = 'NOK'
        # result['valid'] = False
        result['result'] = {"message": "Unauthorized access", "data": []}

        if serializer.is_valid():
            try:
                user_data = authenticate(email=serializer.validated_data['email'],
                                         password=serializer.validated_data['password'])

            except:
                # Response data
                # result['status'] = 'NOK'
                # result['valid'] = False
                result['result']['message'] = 'User not present'
                # Response data
                return Response(result, status=status.HTTP_204_NO_CONTENT)

            if user_data is not None:
                user_details = User.objects.all().filter(email=user_data).values('id', 'name', 'email', 'phone',
                                                                                 'registered_on', 'emp_code'
                                                                                 )
                # print(user_details)
                # if user_data.is_active:
                login(request, user_data)
                data = super(Login, self).post(request)
                data = data.data
                print(data)
                # data['message'] = "Login successfully"
                data['user_info'] = user_details

                # Response data
                result['status'] = "OK"
                result['valid'] = True
                result['result']['message'] = "Login successfully"
                result['result']['data'] = data
                # result['result']['data'] = data
                # Response data
                return Response(result, status=status.HTTP_200_OK)
            else:

                # Response data
                # result['status'] = "NOK"
                # result['valid'] = False
                result['result']['message'] = 'Invalid Credentials'
                # Response data
                return Response(result, status=status.HTTP_422_UNPROCESSABLE_ENTITY)
        # Response data
        # result['status'] = "NOK"
        # result['valid'] = False
        result['result']['message'] = (
                    list(serializer.errors.keys())[0] + ' - ' + list(serializer.errors.values())[0][0]).capitalize()
        # Response data
        return Response(result, status=status.HTTP_422_UNPROCESSABLE_ENTITY)

class Logoutview(LogoutView):
    # permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        result = {}
        # result['status'] = 'NOK'
        # result['valid'] = False
        result['result'] = {"message": "Unauthorized access", "data": []}
        if request.user.is_authenticated:
            try:
                request._auth.delete()
            except:
                # Response data
                # result['status'] = "NOK"
                # result['valid'] = False
                result['result']['message'] = 'Error while logging out'
                # Response data
                return Response(result, status=status.HTTP_200_OK)
            # Response data
            # result['status'] = "OK"
            # result['valid'] = True
            result['result']['message'] = 'Logout successfully !'
            # Response data
            return Response(result, status=status.HTTP_200_OK)



class GetUsersData(APIView):
    permission_classes = [IsAuthenticated]
    serializer_class = UserSerializer

    def get(self, request):
        result = {}
        # result['status'] = "NOK"
        # result['valid'] = False
        result['result'] = {"message": "Unauthorized access", "data": []}

        if request.user.is_authenticated:
            users_data = User.objects.all().exclude(is_deleted=1).values()
            # Response data
            # result['status'] = "OK"
            # result['valid'] = True
            result['result']['message'] = "Data fetched successfully"
            result['result']['data'] = users_data
            # Response data
            return Response(result, status=status.HTTP_200_OK)

    def post(self, request, format=None):
        result = {}
        # result['status'] = "NOK"
        # result['valid'] = False
        result['result'] = {"message": "Unauthorized access", "data": []}

        if request.user.is_authenticated:
            users = request.data['user_id']

            User.objects.filter(id__in=users).delete()
            # Response data
            # result['status'] = "OK"
            # result['valid'] = True
            result['result']['message'] = "User deleted successfully !"
            # Response data
            return Response(result, status=status.HTTP_200_OK)


class DeleteUser(APIView):
    # permission_classes = [IsAuthenticated]
    serializer_class = UserSerializer

    def post(self, request, format=None):
        result = {}
        # result['status'] = "NOK"
        # result['valid'] = False
        result['result'] = {"message": "Unauthorized access", "data": []}

        if request.user.is_authenticated:
            if request.data['ids'] == "":
                result['result']['message'] = "ids cannot be empty"
                return Response(result, status=status.HTTP_401_UNAUTHORIZED)
            else:
                ids = request.data['ids'].split(",")
                qs = User.objects.filter(id__in=ids)
                for obj in qs:
                    temp = User.objects.filter(email=obj).values()
                    # temp.update(is_active=False)
                    temp.update(is_deleted=True)

            # Response data
            # result['status'] = "OK"
            # result['valid'] = True
            result['result']['message'] = "Records deleted successfully"
            # Response data
            return Response(result, status=status.HTTP_200_OK)

# class UpdateUserStatus(APIView):
#     # permission_classes = [IsAuthenticated]
#     serializer_class = UserSerializer

#     def post(self, request, format=None):
#         result = {}
#         result['status'] = "NOK"
#         result['valid'] = False
#         result['result'] = {"message": "Unauthorized access", "data": []}

#         if request.user.is_authenticated:
#             if request.data['ids'] == "":
#                 result['status'] = "OK"
#                 result['valid'] = False
#                 result['result']['message'] = "ids cannot be empty"
#                 return Response(result, status=status.HTTP_422_UNPROCESSABLE_ENTITY)

#             if request.data['status'] == "":
#                 result['result']['message'] = "status cannot be empty"
#                 return Response(result, status=status.HTTP_422_UNPROCESSABLE_ENTITY)

#             user_ids = request.data['ids']
#             user_ids = user_ids.split(",")

#             if len(user_ids) > 0:
#                 data = User.objects.filter(id__in=user_ids)
#                 for i in data:
#                     i.is_active = request.data['status']

#                 User.objects.bulk_update(data, ['is_active'])
#             result['status'] = "OK"
#             result['valid'] = True
#             result['result']['message'] = "Status updated successfully !"

#             return Response(result, status=status.HTTP_200_OK)

