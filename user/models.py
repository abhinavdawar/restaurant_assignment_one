from django.db import models

# Create your models here.

class BaseModel(models.Model):
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True

    def __str__(self):
        return "%s" % self.id

class Customer(BaseModel):
    phone_no = models.CharField(max_length=15, help_text="Phone no with country code")
    email = models.EmailField(null=True)
    name = models.CharField(max_length=50, null=False)
      