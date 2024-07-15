# Generated by Django 5.0.6 on 2024-07-15 07:01

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crudapplication', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserMoreDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone_number', models.CharField(max_length=15)),
                ('address', models.CharField(max_length=100)),
                ('date_of_birth', models.DateField()),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='crudapplication.userdetails')),
            ],
        ),
    ]
