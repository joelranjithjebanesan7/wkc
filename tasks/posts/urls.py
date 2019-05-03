from rest_framework.urlpatterns import format_suffix_patterns
from django.urls import path
from django.conf.urls import url,include 
from rest_framework.routers import DefaultRouter

from posts import views
from .views import CreateUserView

#router = DefaultRouter()
#router.register(r'createuser', CreateUserView)

#urlpatterns = router.urls

urlpatterns = [
    path('posts/', views.PostList.as_view(), name="post-list"),
    path('posts/<int:pk>/', views.PostDetail.as_view()),
    path('user/signup/', views.CreateUserView.as_view()),
    path('followers/', views.FollowersList.as_view()),
    path('followers/<int:pk>/', views.FollowersDetail.as_view()),
    path('like/', views.LikeActivity.as_view()),
    path('like/<int:pk>/', views.LikeDetail.as_view()),
    path('comment/', views.CommentActivity.as_view()),
    path('comment/<int:pk>/', views.CommentDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
