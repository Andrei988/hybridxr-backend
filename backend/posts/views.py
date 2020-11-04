from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .models import Post
from .serializers import PostSerializer, PostCreateSerializer


@api_view(['GET'])
def apiOverview(request):
    api_urls = {
        'Admin page': '/admin/',
        'Create post': '/api/post/create',
        'Post list': '/api/post/list',
    }
    return Response(api_urls)


@api_view(['GET'])
def post_list_view(request, *args, **kwargs):
    qs = Post.objects.all()
    serializer = PostSerializer(qs, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def post_create_view(request, *args, **kwargs):
    context = {
        "request": request
    }
    serializer = PostCreateSerializer(data=request.POST, context=context)
    if serializer.is_valid(raise_exception=True):
        serializer.save()
        return Response(serializer.data, status=201)
    return Response({}, status=400)
