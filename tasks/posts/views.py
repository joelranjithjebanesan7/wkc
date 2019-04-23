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
            followers = self.follow_model.objects.get(follower_id = self.request.user.id) 
            queryset = self.post_model.objects.get(creator__in = followers)
        except self.follow_model.DoesNotExist:
            queryset = None
        return queryset

class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class FollowersList(generics.ListCreateAPIView):
    queryset = Follow.objects.all()
    serializer_class = FollowSerializer

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
