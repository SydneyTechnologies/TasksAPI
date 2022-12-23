from rest_framework import viewsets
from . models import CustomUser
from rest_framework.permissions import IsAuthenticated
from . serializers import CustomUserSerializer, LoginSerializer
from rest_framework.decorators import action
from django.contrib.auth import authenticate, login
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.response import Response
from .exceptions import LoginFailed, UserExists, UserNotFound
from rest_framework import status
from rest_framework.mixins import RetrieveModelMixin
def get_user_tokens(user):
    refresh = RefreshToken.for_user(user)
    return {
        "access_token": str(refresh.access_token),
        "refresh_token": str(refresh)
    }

# here we will implement our own custom view set to handle features like login, registration, change_password, or update the user profile
class UserViewSet(viewsets.GenericViewSet):
    # first lets create the login view
    queryset = CustomUser.objects.all()

    def get_serializer_class(self):
        if self.action == "login":
           return LoginSerializer
        elif self.action == "register":
            return CustomUserSerializer
        else:
            return CustomUserSerializer

    @action(detail=False, methods=["POST"])
    def login(self, request):
        username = request.data.get("username", None)
        password = request.data.get("password", None)
        if username and password:
            user = authenticate(request, username=username, password=password)
            login(request=request, user=user)

            if user:
                return Response(get_user_tokens(user))
            else:
                raise LoginFailed
        else:
            return Response({"detail":"credentials missing"}, status=status.HTTP_400_BAD_REQUEST)
    
    @action(detail=False, methods=["POST"])
    def register(self, request):
        email = request.data.get("email")
        # first lets check if the user already exists in our database
        try:
            user = CustomUser.objects.get(email=email)
            if user:
                raise UserExists
        except:
            # so if user does not exist then lets create a new user
            # this here will create a new user 
            serializer = CustomUserSerializer(data=request.data)
            if serializer.is_valid():
                user = serializer.save()
            response = get_user_tokens(user)
            response["detail"] = "Registration Successful"
        return Response(response, status=status.HTTP_201_CREATED)


    @action(detail=False, methods=["GET"])
    def data(self, request):
        try:
            return Response(CustomUserSerializer(request.user).data)
        except:
            raise UserNotFound
        # try:
        #     user = CustomUser.objects.get(email=pk)
        #     return Response(user)
        # except:
        #     raise UserNotFound

        
    






    