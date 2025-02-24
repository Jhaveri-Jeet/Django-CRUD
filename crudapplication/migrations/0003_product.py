# Generated by Django 5.0.6 on 2024-07-16 13:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crudapplication', '0002_usermoredetails'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=200)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('image', models.ImageField(upload_to='images/')),
            ],
        ),
    ]
