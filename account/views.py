from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated

from .models import User, Order, Product
from .serializers import UserGetSerializer, UserSerializer, OrderSerializer, ProductSerializer


class UserView(APIView):
    def get(self, request):
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
    permission_classes = [IsAuthenticated]

    def get(self, request, pk):
        user = User.objects.get(pk=pk)
        serializer = UserGetSerializer(user)
        return Response(serializer.data)

class ProductView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class OrderView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        orders = Order.objects.all()
        serializer = OrderSerializer(orders, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = OrderSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class AdminOrderview(APIView):
    def get(self, request):
        orders = Order.objects.all()
        serializer = OrderSerializer(orders, many=True)
        return Response(serializer.data)

class OrderDetailView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request, pk):
        orders = Order.objects.filter(user=pk)
        serializer = OrderSerializer(orders, many=True)
        return Response(serializer.data)