# Generated by Django 4.1.2 on 2022-10-23 06:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Professor',
        ),
        migrations.DeleteModel(
            name='Student',
        ),
        migrations.DeleteModel(
            name='Teacher',
        ),
    ]
