# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.contrib.auth.models import User
   
class Post(models.Model):
    creator = models.ForeignKey(User, related_name='creator_post_set', null=True, on_delete=models.CASCADE)
    title = models.CharField(max_length=25)
    created_date = models.DateTimeField(auto_now_add=True)
    content = models.TextField()
    likes = models.BigIntegerField(null=True)
    comments = models.BigIntegerField(null=True)

class Follow(models.Model):
    follower = models.ForeignKey(User, related_name='following', null=True, on_delete=models.CASCADE)
    followed_on = models.DateTimeField(auto_now_add=True)
    following = models.ForeignKey(User, related_name='follower',null=True, on_delete=models.CASCADE)

class Like(models.Model):
    post = models.ForeignKey(Post, null=True, on_delete=models.CASCADE)
    is_liked = models.BooleanField(null=True)
    liked_by = models.ForeignKey(User, related_name='liked_activity_set', null=True, on_delete=models.CASCADE)
    liked_on = models.DateTimeField(auto_now=True)

class Comment(models.Model):
    post = models.ForeignKey(Post, null=True, on_delete=models.CASCADE)
    comment_msg = models.TextField(null=True)
    comment_by = models.ForeignKey(User, related_name='comment_activity_set', null=True, on_delete=models.CASCADE)
    commented_on = models.DateTimeField(auto_now=True)

