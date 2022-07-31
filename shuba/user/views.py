from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import action
from rest_framework import viewsets, permissions
from user.models import User


from .serializers import RegistrationSerializer,  UserSerializer



class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated, ]
    queryset = User.objects

    permission_classes_by_action = {
        "create": [permissions.AllowAny, ],
    }

    def get_permissions(self):
        if self.action in self.permission_classes_by_action:
            permissions = self.permission_classes_by_action[self.action]
        else:
            permissions = self.permission_classes
        return [permission() for permission in permissions]

    def get_serializer_class(self):
        if self.action == "create":
            return RegistrationSerializer
        return self.serializer_class

    @action(methods=["GET"], detail=False)
    def me(self, request):
        user = request.user
        serializer = self.get_serializer(instance=user)
        return Response(data=serializer.data, status=status.HTTP_200_OK)


