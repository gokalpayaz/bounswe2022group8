# Generated by Django 4.0.4 on 2022-05-11 09:54

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('api', '0002_comment_created_at_comment_updated_at_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='myuser',
            name='email',
            field=models.EmailField(default='email@mail.com', max_length=254, unique=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='myuser',
            name='followers',
            field=models.ManyToManyField(related_name='followed_by', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='myuser',
            name='followes',
            field=models.ManyToManyField(related_name='follows', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='myuser',
            name='name',
            field=models.CharField(default='John', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='myuser',
            name='surname',
            field=models.CharField(default='WashingMachine', max_length=100),
            preserve_default=False,
        ),
    ]
