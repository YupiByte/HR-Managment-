# Generated by Django 4.2.6 on 2023-12-15 13:07

import django.core.validators
from django.db import migrations, models
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_alter_employee_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='employee_type',
            field=models.CharField(choices=[('CEO', 'Chief Executive Officer'), ('Vice President', 'Vice President'), ('Software Engineer', 'Software Engineer'), ('System Administrator', 'System Administrator'), ('QA Engineer', 'QA Engineer'), ('Director', 'Director'), ('Manager', 'Manager'), ('Administrator', 'Administrator'), ('HR Administrator', 'HR Administrator'), ('Intern', 'Intern')], max_length=30),
        ),
        migrations.AlterField(
            model_name='employee',
            name='first_name',
            field=models.CharField(max_length=150, validators=[django.core.validators.RegexValidator('^[a-zA-ZñÑáéíóúüÁÉÍÓÚÜ\\s]+$')]),
        ),
        migrations.AlterField(
            model_name='employee',
            name='last_name',
            field=models.CharField(max_length=150, validators=[django.core.validators.RegexValidator('^[a-zA-ZñÑáéíóúüÁÉÍÓÚÜ\\s]+$')]),
        ),
        migrations.AlterField(
            model_name='employee',
            name='phone',
            field=phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None),
        ),
    ]