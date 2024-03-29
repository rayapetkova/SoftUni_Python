# Generated by Django 4.2.4 on 2023-11-07 21:11

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_alter_customer_phone_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='name',
            field=models.CharField(max_length=100, validators=[django.core.validators.RegexValidator(message='Name can only contain letters and spaces', regex='[A-Za-z\\s]+')]),
        ),
    ]
