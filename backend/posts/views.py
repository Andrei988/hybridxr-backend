from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.utils import json
from django.core.mail import send_mail

from .models import Post, CompanyData
from .serializers import PostSerializer, CompanyDataSerializer


@api_view(['GET'])
def apiOverview(request):
    api_urls = {
        'admin': '/api/admin',
        'contact_view': '/api/contact',
        'get_company_info': '/api/info',
        'post_list_view': '/api/post/list',
        'post_detailed_view': '/api/post/:id',
    }
    return Response(api_urls)


@api_view(['POST'])
def contact_view(request, *args, **kwargs):
    body_unicode = request.body.decode('utf-8')
    body = json.loads(body_unicode)
    send_mail(
        body['subject'],
        body['textarea'],
        body['email'],
        ['andreimain03@gmail.com'],  # TODO: change to working email
        fail_silently=False,
    )

    return Response({'message': 'message sent'}, status=200)


@api_view(['GET'])
def company_info_view(request, *args, **kwargs):
    qs = CompanyData.objects.all()
    serializer = CompanyDataSerializer(qs, many=True)
    return Response(serializer.data, status=200)


@api_view(['GET'])
def post_list_view(request, *args, **kwargs):
    qs = Post.objects.all()
    if qs.count() is 0:
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
