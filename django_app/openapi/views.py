from rest_framework import filters
from rest_framework import viewsets

from .models import Performance
from .serializers import OpenApiSerializer


class SnippetViewSet(viewsets.ModelViewSet):
    queryset = Performance.objects.all()
    serializer_class = OpenApiSerializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ('seq', 'title', 'start_date', 'end_date', 'place', 'realm_name',
                     'area', 'price', 'phone')

class DetailViewSet(viewsets.ModelViewSet):
    queryset = Performance.objects.all()
    serializer_class = OpenApiSerializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ('seq', 'title')


class AreaViewSet(viewsets.ModelViewSet):
    queryset = Performance.objects.all()
    serializer_class = OpenApiSerializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ('area', 'area')


class GenreViewSet(viewsets.ModelViewSet):
    queryset = Performance.objects.all()
    serializer_class = OpenApiSerializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ('realm_name', 'realm_name')

