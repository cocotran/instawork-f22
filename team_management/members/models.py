from django.db import models


# Create your models here.
class Member(models.Model):
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    phone_number = models.CharField(max_length=10, unique=True)
    email = models.CharField(max_length=64, unique=True)
    role = models.CharField(max_length=64, default="regular")

    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name}-{self.phone_number}-{self.email}-{self.role}"

    @staticmethod
    def is_valid_request(member: dict) -> tuple:
        """Returns (is_valid, error)"""
        required_fields = ["first_name", "last_name", "phone_number", "email"]
        for field in required_fields:
            if member.get(field, "") == "":
                return (False, f"Missing value for {field}")

        # TODO: validate all fields

        return (True, "")
