# Generated by Django 3.2.3 on 2021-12-29 07:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task1', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='sellerprofile',
            old_name='city',
            new_name='product',
        ),
        migrations.RemoveField(
            model_name='sellerprofile',
            name='cnic',
        ),
        migrations.RemoveField(
            model_name='sellerprofile',
            name='state',
        ),
        migrations.AddField(
            model_name='sellerprofile',
            name='product_price',
            field=models.PositiveIntegerField(default=None, max_length=30),
        ),
        migrations.AddField(
            model_name='sellerprofile',
            name='quantity',
            field=models.PositiveIntegerField(default=None, max_length=30),
        ),
    ]
