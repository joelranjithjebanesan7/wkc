from django.shortcuts import render
from rest_framework import generics
from django.contrib.auth.models import User
from rest_framework.mixins import CreateModelMixin
from rest_framework.viewsets import GenericViewSet
from django.core.exceptions import ObjectDoesNotExist

from posts.models import Post, Follow, Like, Comment
from posts.serializers import UserSerializer, PostSerializer, PostListSerializer, FollowSerializer, LikeSerializer, CommentSerializer


class CreateUserView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class PostList(generics.ListCreateAPIView):
    serializer_class = PostListSerializer
    follow_model = FollowSerializer.Meta.model
    post_model = PostSerializer.Meta.model
    def get_queryset(self):
        try:
           following = self.request.user.following.all().values_list('following', flat=True)  # because of related name
           queryset = self.post_model.objects.filter(creator_id__in = list(following)) | self.post_model.objects.filter (creator = self.request.user) 
        except self.follow_model.DoesNotExist:
            queryset = None
        return queryset

class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class FollowersList(generics.ListCreateAPIView):
    #queryset = Follow.objects.all()
    serializer_class = FollowSerializer
    def get_queryset(self):
        queryset = Follow.objects.filter(follower=self.request.user)
        return queryset 

class FollowersDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Follow.objects.all()
    serializer_class = FollowSerializer

class LikeActivity(generics.CreateAPIView):
    queryset = Like.objects.all()
    serializer_class = LikeSerializer

class LikeDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Like.objects.all()
    serializer_class = LikeSerializer

class CommentActivity(generics.CreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

class CommentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
