# Generated by Django 3.2.8 on 2021-12-06 07:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_alter_orderitemmodel_created_on'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='OrderModel',
            new_name='Order',
        ),
        migrations.RenameModel(
            old_name='OrderItemModel',
            new_name='OrderItem',
        ),
        migrations.RenameModel(
            old_name='ProductModel',
            new_name='Product',
        ),
    ]