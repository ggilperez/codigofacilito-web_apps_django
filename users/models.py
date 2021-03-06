from django.contrib.auth.models import AbstractUser
from django.db import models

from orders.common import OrderStatus
from stripeAPI.customer import create_customer


# AbstractBaseUser
# id
# password
# last_login

# AbstractUser
# username
# first_name
# last_name
# email
# password
# groups
# user_permissions
# is_staff
# is_active
# is_superuser
# last_login
# date_joined


class User(AbstractUser):
    customer_id = models.CharField(max_length=100, blank=True, null=True)

    def get_full_name(self):
        return f'{self.first_name} {self.last_name}'

    @property
    def shipping_address(self):
        return self.shippingaddress_set.filter(default=True).first()

    @property
    def billing_profile(self):
        return self.billingprofile_set.filter(default=True).first()

    @property
    def description(self):
        return "Descripcion para el usuario {}".format(self.username)

    def has_customer(self):
        return self.customer_id is not None

    def create_customer_id(self):
        if not self.has_customer():
            customer = create_customer(self)
            self.customer_id = customer.id
            self.save()

    def has_billing_profiles(self):
        return self.billingprofile_set.exists()

    def has_shipping_address(self):
        return self.shipping_address is not None

    def orders_completed(self):
        return self.order_set.filter(status=OrderStatus.COMPLETED).order_by('-id')

    def has_shipping_addresses(self):
        return self.shippingaddress_set.exists()

    @property
    def addresses(self):
        return self.shippingaddress_set.all()

    @property
    def billing_profiles(self):
        return self.billingprofile_set.all().order_by('-default')


class Customer(User):
    class Meta:
        proxy = True

    def get_product(self):
        return []


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField()
