# Generated by Django 2.1 on 2019-04-22 18:04

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0005_auto_20190422_1704'),
    ]

    operations = [
        migrations.AlterField(
            model_name='follow',
            name='follower',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='following', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='follow',
            name='following',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='follower', to=settings.AUTH_USER_MODEL),
        ),
    ]
