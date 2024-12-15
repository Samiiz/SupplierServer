from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import User
from .serializers import UserSerializer, UserGetSerializer


class UserView(APIView):
    def get(self, request):
        # if pk in request.data:
        #     user = User.objects.get(pk=pk)
        #     serializer = UserSerializer(user)
        #     return Response(serializer.data)
        user = User.objects.all()
        serializer = UserGetSerializer(user, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserDetailView(APIView):
    serializer_class = UserGetSerializer

    def get(self, request, pk):
        user = User.objects.get(pk=pk)
        serializer = UserGetSerializer(user)
        return Response(serializer.data)
