# Generated by Django 2.1 on 2019-04-21 08:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Activity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment_msg', models.TextField(null=True)),
                ('liked_on', models.DateTimeField(auto_now=True)),
                ('commented_on', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Posts',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title_name', models.CharField(max_length=25)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('content', models.TextField()),
                ('likes', models.BigIntegerField()),
                ('comments', models.BigIntegerField()),
            ],
        ),
        migrations.AddField(
            model_name='activity',
            name='post',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='posts.Posts'),
        ),
    ]
