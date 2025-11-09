from rest_framework import generics
from rest_framework.permissions import IsAuthenticated, IsAdminUser

from posts.models import Post, Comment
from posts.paginators import PostCommentPagination
from posts.permissions import IsOwner
from posts.serializers import PostSerializer, CommentSerializer


# Create your views here.
class PostCreateAPIView(generics.CreateAPIView):
    '''Создание поста'''
    serializer_class = PostSerializer

    def perform_create(self, serializer):
        post = serializer.save(owner=self.request.user)


class PostListAPIView(generics.ListAPIView):
    '''Просмотр всех постов'''
    serializer_class = PostSerializer
    queryset = Post.objects.all()
    pagination_class = PostCommentPagination


class PostRetrieveAPIView(generics.RetrieveAPIView):
    '''Просмотр поста'''
    serializer_class = PostSerializer
    queryset = Post.objects.all()


class PostUpdateAPIView(generics.UpdateAPIView):
    '''Обновление инф. поста'''
    serializer_class = PostSerializer
    queryset = Post.objects.all()
    permission_classes = [IsOwner, IsAdminUser, ]


class PostDestroyAPIView(generics.DestroyAPIView):
    '''Удаление поста'''
    queryset = Post.objects.all()
    permission_classes = [IsOwner, IsAdminUser, ]


class CommentCreateAPIView(generics.CreateAPIView):
    '''Создание комментария'''
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated, ]

    def perform_create(self, serializer):
        comment = serializer.save(owner=self.request.user)


class CommentListAPIView(generics.ListAPIView):
    '''Просмотр всех комментариев'''
    serializer_class = CommentSerializer
    queryset = Comment.objects.all()
    pagination_class = PostCommentPagination


class CommentRetrieveAPIView(generics.RetrieveAPIView):
    '''Просмотр комментария'''
    serializer_class = CommentSerializer
    queryset = Comment.objects.all()


class CommentUpdateAPIView(generics.UpdateAPIView):
    '''Обновление инф. комментария'''
    serializer_class = CommentSerializer
    queryset = Comment.objects.all()
    permission_classes = [IsOwner, IsAdminUser, ]


class CommentDestroyAPIView(generics.DestroyAPIView):
    '''Удаление комментария'''
    queryset = Comment.objects.all()
    permission_classes = [IsOwner, IsAdminUser, ]
