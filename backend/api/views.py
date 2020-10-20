"""
Views for calorie-counter API
"""

from django.contrib.auth import authenticate, get_user_model
from django.forms.models import model_to_dict
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view, permission_classes
from rest_framework.parsers import JSONParser
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import status


@api_view(['POST'])
@permission_classes((AllowAny,))
def signup(request):
    """
    Sign up a new user
    """
    user_info = JSONParser().parse(request)
    if 'username' not in user_info or 'password' not in user_info or 'email' not in user_info:
        return Response({"detail": "username, password, or email not provided"}, status=status.HTTP_400_BAD_REQUEST)

    username, password, email = user_info['username'], user_info['password'], user_info['email']
    try:
        get_user_model().objects.get(username=username)
        return Response({"detail": "username already exists"}, status=status.HTTP_400_BAD_REQUEST)
    except get_user_model().DoesNotExist:
        pass

    user = get_user_model().objects.create_user(username=username, email=email, password=password)
    return Response(model_to_dict(user), status=status.HTTP_201_CREATED)

@api_view(['GET'])
def closeaccount(request):
    """
    Delete logged in user account
    """
    get_user_model().objects.get(username=request.user.get_username()).delete()
    return Response({}, status=status.HTTP_200_OK)

@api_view(["POST"])
@permission_classes((AllowAny,))
def login(request):
    """
    Log in with credentials and get authtoken
    """
    username = request.data.get("username")
    password = request.data.get("password")
    if not username or not password:
        return Response({"detail": "username or password not provided"}, status=status.HTTP_400_BAD_REQUEST)

    user = authenticate(username=username, password=password)
    if not user:
        return Response({"detail": "Invalid Credentials"}, status=status.HTTP_404_NOT_FOUND)

    token, _ = Token.objects.get_or_create(user=user)
    return Response({'token': token.key}, status=status.HTTP_200_OK)

@api_view(["GET"])
def logout(request):
    """
    Logout current logged in user account
    """
    request.user.auth_token.delete()
    return Response({}, status=status.HTTP_200_OK)
