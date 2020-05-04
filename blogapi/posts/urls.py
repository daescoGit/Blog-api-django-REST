# from django.urls import path
from rest_framework.routers import SimpleRouter  # alt DefaultRouter / custom

from .views import UserViewSet, PostViewSet

# router complementing viewsets
router = SimpleRouter()
router.register('users', UserViewSet, base_name='users')
router.register('', PostViewSet, base_name='posts')

# using route
urlpatterns = router.urls

# basic individual urls
# class based import (as_view)
"""
urlpatterns = [
    path('', PostList.as_view()),
    path('<int:pk>/', PostDetail.as_view()),
    path('users/', UserList.as_view()),
    path('users/<int:pk>/', UserDetail.as_view()),

]
"""
