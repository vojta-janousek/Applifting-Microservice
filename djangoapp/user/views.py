from rest_framework import generics, permissions
from django.contrib.auth import get_user_model

from user.serializers import UserSerializer


class CreateUserView(generics.CreateAPIView):
    '''
    Create a new user in the system.
    '''
    serializer_class = UserSerializer


class ManagerUserView(generics.RetrieveUpdateAPIView):
    '''
    Manage the authenticated user.
    '''
    serializer_class = UserSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def get_object(self):
        '''
        Retrieve and return authenticated user.
        '''
        return self.request.user
