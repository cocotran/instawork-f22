from django.db import models


ROLES = [
    ("admin", "Admin - Can delete members"),
    ("regular", "Regular - Can't delete members"),
]

# Create your models here.
class Member(models.Model):
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    phone_number = models.CharField(max_length=10, unique=True)
    email = models.CharField(max_length=64, unique=True)
    role = models.CharField(max_length=64, choices=ROLES, default="regular")

    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name}-{self.phone_number}-{self.email}-{self.role}"
