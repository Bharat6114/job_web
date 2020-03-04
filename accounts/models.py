
from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

GENDER_CHOICES = (
    ('male', 'Male'),
    ('female', 'Female'))


class User(AbstractUser):
    ROLES = (("0", "Admin"), ("1", "Employer"), ("2", "Employee"),("3","Guest"))
    role = models.CharField(max_length=1, choices=ROLES, default="2")
    email = models.EmailField(verbose_name="email address", max_length=255, unique=True,)
    gender = models.CharField(max_length=10, blank=True, null=True, default="")

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = "username", "role", "first_name", "last_name","gender"

    def __str__(self):
        return self.username


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    dob = models.DateField(null=True)
    contact_num = models.CharField(max_length=15, null=True)
    address = models.CharField(max_length=255, null=False)