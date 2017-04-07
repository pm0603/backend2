from rest_framework import serializers

from .models import Performance


class OpenApiSerializer(serializers.ModelSerializer):
    class Meta:
        model = Performance
        fields = ('seq', 'title', 'start_date', 'end_date', 'place', 'realm_name',
                  'area', 'price', 'content', 'ticket_url', 'phone', 'thumbnail',
                  'place_url', 'place_addr', 'gps_x', 'gps_y')
