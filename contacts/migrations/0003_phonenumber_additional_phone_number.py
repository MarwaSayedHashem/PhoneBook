# Generated by Django 5.0.6 on 2024-05-27 18:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0002_phonenumber_address_phonenumber_country_code_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='phonenumber',
            name='additional_phone_number',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]
