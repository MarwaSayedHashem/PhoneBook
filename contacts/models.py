from django.db import models

class Contact(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class PhoneNumber(models.Model):
    contact = models.ForeignKey(Contact, related_name='phone_numbers', on_delete=models.CASCADE)
    number = models.CharField(max_length=15)
    country_code = models.CharField(max_length=5, blank=True, null=True)
    address = models.CharField(max_length=255, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    gender = models.CharField(max_length=10, blank=True, null=True)

    def __str__(self):
        return f"{self.number} ({self.contact.name})"
