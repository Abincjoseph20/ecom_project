# Generated by Django 5.0.6 on 2024-06-24 10:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ecom_app1', '0003_products_delete_product'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Products',
            new_name='Product',
        ),
    ]
