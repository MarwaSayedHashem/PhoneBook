from django.db import models


class Contact(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class PhoneNumber(models.Model):
    GENDER_CHOICES = [
        ('male', 'Male'),
        ('female', 'Female'),
        ('rather_not_say', 'Rather not say')
    ]
    contact = models.ForeignKey(Contact, related_name='phone_numbers', on_delete=models.CASCADE)
    number = models.CharField(max_length=15)
    country_code = models.CharField(max_length=5, blank=True, null=True)
    address = models.CharField(max_length=255, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    gender = models.CharField(max_length=15, choices=GENDER_CHOICES)

    def __str__(self):
        return f"{self.number} ({self.contact.name})"


class AdditionalPhoneNumber(models.Model):
    contact = models.ForeignKey(Contact, related_name='additional_phone_numbers', on_delete=models.CASCADE)
    additional_number = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.additional_number} ({self.contact.name})"
