from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from .views import UserDetailView, UserView, ProductView, OrderView, OrderDetailView, AdminOrderview

urlpatterns = [
    path("users/", UserView.as_view(), name="user"),
    path("users/<int:pk>/", UserDetailView.as_view(), name="user-detail"),
    path("users/login/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("users/login/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("products/", ProductView.as_view(), name="products"),
    path("orders/", OrderView.as_view(), name="orders"),
    path("orders/<int:pk>/", OrderDetailView.as_view(), name="order-detail"),
    path('admin/orders/', AdminOrderview.as_view(), name='admin-orders'),
]

