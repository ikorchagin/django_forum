# Generated by Django 3.0 on 2019-12-08 09:19

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Articles', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rubric',
            name='url',
            field=models.CharField(max_length=15, validators=[django.core.validators.RegexValidator(message='Только латинские буквы и цифры!', regex='[0-9a-zA-Z]')]),
        ),
    ]
