from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.utils import json
from django.core.mail import send_mail

from .models import Post
from .serializers import PostSerializer


@api_view(['GET'])
def apiOverview(request):
    api_urls = {
        'Admin page': '/admin/',
        'Post list': '/api/post/list',
        'Post detailed': '/api/post/:id',
    }
    return Response(api_urls)


@api_view(['POST'])
def contact_view(request, *args, **kwargs):
    body_unicode = request.body.decode('utf-8')
    body = json.loads(body_unicode)
    print(body)
    send_mail(
        body['subject'],
        body['textarea'],
        body['email'],
        ['andreimain03@gmail.com'],
        fail_silently=False,
    )

    return Response()


@api_view(['GET'])
def get_company_info(request, *args, **kwargs):
    return Response()


@api_view(['GET'])
def post_list_view(request, *args, **kwargs):
    qs = Post.objects.all()
    if qs is None:
        return Response({}, status=404)
    serializer = PostSerializer(qs, many=True)
    return Response(serializer.data, status=200)


@api_view(['GET'])
def post_detailed_view(request, pk, *args, **kwargs):
    qs = Post.objects.filter(id=pk)
    if qs is None:
        return Response({}, status=404)
    serializer = PostSerializer(qs, many=True)
    return Response(serializer.data, status=200)
