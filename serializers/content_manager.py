from rest_framework import serializers
from content_manager.models import City, Segment, MobileOperator


class CityJSON(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = ['id', 'name']


class SegmentJSON(serializers.ModelSerializer):
    class Meta:
        model = Segment
        fields = ['id', 'name']


class MobileOperatorJSON(serializers.ModelSerializer):
    class Meta:
        model = MobileOperator
        fields = ['id', 'name', 'bg_color', 'font_color']
