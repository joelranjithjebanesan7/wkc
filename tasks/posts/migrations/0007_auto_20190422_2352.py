# Generated by Django 2.1 on 2019-04-22 23:52

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('posts', '0006_auto_20190422_1804'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment_msg', models.TextField(null=True)),
                ('commented_on', models.DateTimeField(auto_now=True)),
                ('comment_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='comment_activity_set', to=settings.AUTH_USER_MODEL)),
                ('post', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='posts.Post')),
            ],
        ),
        migrations.CreateModel(
            name='Like',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('liked_on', models.DateTimeField(auto_now=True)),
                ('liked_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='liked_activity_set', to=settings.AUTH_USER_MODEL)),
                ('post', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='posts.Post')),
            ],
        ),
        migrations.RemoveField(
            model_name='activity',
            name='liked_by',
        ),
        migrations.RemoveField(
            model_name='activity',
            name='post',
        ),
        migrations.DeleteModel(
            name='Activity',
        ),
    ]