import uuid
from django.db import models
from user.models import BaseModel, Customer

# Create your models here.

class Category(BaseModel):

    NATIONALITY_INDIAN = "indian"
    NATIONALITY_CHINESE = "chinese"
    NATIONALITY_THAI = "thai"
    NATIONALITY_JAPANESE = "japanese"

    NATIONALITY_CHOICES = (
        (NATIONALITY_INDIAN, NATIONALITY_INDIAN),
        (NATIONALITY_CHINESE, NATIONALITY_CHINESE),
        (NATIONALITY_JAPANESE, NATIONALITY_JAPANESE),
        (NATIONALITY_THAI, NATIONALITY_THAI)
    )

    is_veg = models.BooleanField(default=True)
    nationality = models.CharField(max_length=50, choices=NATIONALITY_CHOICES, default=NATIONALITY_INDIAN)


class Product(BaseModel):
    category = models.ForeignKey('Category', related_name="using_products", on_delete=models.CASCADE)
    dish_name = models.CharField(max_length=100, null=False)
    price = models.DecimalField(max_digits=10, decimal_places=2)


class Order(BaseModel):
    order_id = models.UUIDField(default=uuid.uuid4, unique=True)
    total_payment = models.DecimalField(max_digits=10, decimal_places=2)
    paid_in_advance = models.BooleanField(default=True)
    product = models.ForeignKey('Product', on_delete=models.CASCADE)
    customer = models.ForeignKey('user.Customer', on_delete=models.CASCADE, default=1)
