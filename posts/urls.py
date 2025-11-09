from django.urls import path
from rest_framework.routers import DefaultRouter

from posts.views import PostCreateAPIView, PostDestroyAPIView, PostUpdateAPIView, PostListAPIView, PostRetrieveAPIView, \
    CommentListAPIView, CommentCreateAPIView, CommentDestroyAPIView, CommentUpdateAPIView, CommentRetrieveAPIView

app_name = 'posts'

router = DefaultRouter()

urlpatterns = [
                  path('', PostListAPIView.as_view(), name='post_list'),
                  path('create/', PostCreateAPIView.as_view(), name='post_create'),
                  path('update/<int:pk>', PostUpdateAPIView.as_view(), name='post_update'),
                  path('<int:pk>', PostRetrieveAPIView.as_view(), name='post'),
                  path('delete/<int:pk>', PostDestroyAPIView.as_view(), name='post_delete'),
                  path('comments/', CommentListAPIView.as_view(), name='comment_list'),
                  path('comments/create/', CommentCreateAPIView.as_view(), name='comment_create'),
                  path('comments/update/<int:pk>', CommentUpdateAPIView.as_view(),
                       name='comment_update'),
                  path('comments/<int:pk>', CommentRetrieveAPIView.as_view(), name='comment'),
                  path('comments/delete/<int:pk>', CommentDestroyAPIView.as_view(),
                       name='comment_delete'),
              ] + router.urls
