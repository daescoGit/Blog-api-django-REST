# basic generic CRUD (UNUSED)
from rest_framework import generics  # , permissions
# viewset CRUD
from rest_framework import viewsets
# for getting user info
from django.contrib.auth import get_user_model

from .models import Post
from .serializers import PostSerializer, UserSerializer
from .permissions import IsAuthorOrReadOnly


# viewsets, additional settings is required.
# Suitable for many endpoints with repetition / consistent url config
class PostViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthorOrReadOnly,)
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer


# UNUSED individual views
# ListCreateAPIView = list all avail as read, write endpoint
# queryset, serializer_class = pre def base attributes
class PostList(generics.ListCreateAPIView):
    # per view level based permission, alt: project level (losen here instead - safer)
    # permission_classes = (permissions.IsAuthenticated,)  # touple is defined by comma, not para ()
    queryset = Post.objects.all()
    serializer_class = PostSerializer


# RetrieveUpdateDestroyAPIView = individual as read, update, delete endpoint
class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthorOrReadOnly,)  # our custom permisson
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class UserList(generics.ListCreateAPIView):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer

