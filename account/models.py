from django.contrib.auth.models import AbstractBaseUser, UserManager
from django.db import models
from django.db.models import Manager


# Create your models here.
class Common(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class User(AbstractBaseUser, Common):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    address = models.TextField()
    affiliation = models.CharField(max_length=100)
    api = models.TextField()

    last_login = None

    objects = UserManager()

    USERNAME_FIELD = "email"

    def __str__(self):
        return f"USER: {self.email}"

    class Meta:
        db_table = "users"
        ordering = ["id"]


class Product(Common):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    objects = Manager()

    def __str__(self):
        return f"PRODUCT: {self.name}"

    class Meta:
        db_table = "products"
        ordering = ["id"]


class Order(Common):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()

    def __str__(self):
        return f"ORDER: {self.user.affiliation} / {self.user.name} / {self.product.name} / {self.quantity}"

    class Meta:
        db_table = "orders"
        ordering = ["id"]
