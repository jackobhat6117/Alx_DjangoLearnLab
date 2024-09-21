from django.shortcuts import render
from rest_framework import viewsets,permissions
from .models import Post, Comment
from .serializers import PostSerializer, CommentSerializer
from rest_framework import filters, response
from rest_framework.views import APIView

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all().order_by('created_at')
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    filter_backends = [filters.SearchFilter]
    search_fields = ['title', 'content']

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user) 


class UserFeedView(APIView):

    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        following_user = request.user.following.all()
        posts = Post.objects.filter(author__in = following_user).order_by('-created_at')

        posts = posts[:50]

        serializer = PostSerializer(posts, many = True)
        return response.Response(serializer.data)
