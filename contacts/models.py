from django.db import models
from django.core.validators import RegexValidator


class Contact(models.Model):
    """Contact Details."""

    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    phone = models.CharField(
        max_length=24, validators=[RegexValidator(r'\d+')])
    email = models.EmailField(blank=True)
    address = models.CharField(max_length=256)

    def __str__(self):
        return self.first_name + " " + self.last_name
