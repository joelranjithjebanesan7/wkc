# Generated by Django 2.1 on 2019-04-23 00:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0007_auto_20190422_2352'),
    ]

    operations = [
        migrations.AddField(
            model_name='like',
            name='is_liked',
            field=models.BooleanField(null=True),
        ),
    ]
