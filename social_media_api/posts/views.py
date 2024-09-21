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
        # Get the users that the current user is following
        following_users = request.user.following.all()

        # Query posts from followed users, ordered by creation date (most recent first)
        posts = Post.objects.filter(author__in=following_users).order_by('-created_at')
        
        # Serialize the posts data
        serializer = PostSerializer(posts, many=True)
        
        # Return the serialized data in the response
        return response.Response(serializer.data)