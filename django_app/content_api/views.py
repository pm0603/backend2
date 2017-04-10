from content_api.models import Content
from rest_framework import filters
from rest_framework import viewsets

from .serializers import ContentSerializer


class SnippetViewSet(viewsets.ModelViewSet):
    queryset = Content.objects.all()
    serializer_class = ContentSerializer
    filter_backends = (filters.OrderingFilter, filters.SearchFilter)
    ordering = ('-start_date',)
    search_fields = ('seq', 'title', 'start_date', 'end_date', 'place', 'realm_name',
                     'area', 'price', 'phone')


class DetailViewSet(viewsets.ModelViewSet):
    queryset = Content.objects.all()
    serializer_class = ContentSerializer
    filter_backends = (filters.OrderingFilter, filters.SearchFilter)
    ordering = ('-start_date',)
    search_fields = ('seq', 'title')


class AreaViewSet(viewsets.ModelViewSet):
    queryset = Content.objects.all()
    serializer_class = ContentSerializer
    filter_backends = (filters.OrderingFilter, filters.SearchFilter)
    ordering = ('-start_date',)
    search_fields = ('area', 'area')


class GenreViewSet(viewsets.ModelViewSet):
    queryset = Content.objects.all()
    serializer_class = ContentSerializer
    filter_backends = (filters.OrderingFilter, filters.SearchFilter)
    ordering = ('-start_date',)
    search_fields = ('realm_name', 'realm_name')
