from rest_framework import serializers
from posts.models import Post, Follow, Like, Comment
from rest_framework.serializers import ModelSerializer
from django.contrib.auth.models import User

#UserModel = get_user_model()

class UserSerializer(ModelSerializer):
    password = serializers.CharField(write_only=True)

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            password=validated_data['password'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
        )
        return user

    class Meta:
        model = User
        fields = ( 'username', 'first_name', 'last_name','password',)
        write_only_fields = ('password',)

class PostListSerializer(serializers.ModelSerializer):
    creator = serializers.HiddenField(
              default=serializers.CurrentUserDefault()
              )
    class Meta:
        model = Post
        fields = ['title', 'content', 'created_date', 'creator',]

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['title', 'content']

class FollowSerializer(serializers.ModelSerializer):
    follower = serializers.HiddenField(
              default=serializers.CurrentUserDefault()
              )
    class Meta:
        model = Follow
        fields = '__all__'


class LikeSerializer(serializers.ModelSerializer):
    liked_by = serializers.HiddenField(
              default=serializers.CurrentUserDefault()
              )
    class Meta:
        model = Like
        fields = ['post', 'liked_by',]

class CommentSerializer(serializers.ModelSerializer):
    comment_by = serializers.HiddenField(
              default=serializers.CurrentUserDefault()
              )
    class Meta:
        model = Comment
        fields = ['post', 'comment_msg', 'comment_by']
