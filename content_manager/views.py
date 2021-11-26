from rest_framework.response import Response
from rest_framework.views import APIView
from .services import content_manager
from serializers.content_manager import CityJSON, SegmentJSON, MobileOperatorJSON


class CitiesListView(APIView):
    def get(self, request):
        cities_queryset = content_manager.get_cities()
        cities_serializer = CityJSON(cities_queryset, many=True)
        return Response(cities_serializer.data)


class CityView(APIView):
    def get(self, request, pk: int):
        city_queryset = content_manager.get_city(pk)
        city_serializer = CityJSON(city_queryset, many=False)
        return Response(city_serializer.data)


class SegmentsListView(APIView):
    def get(self, request, pk=None):
        segments_queryset = content_manager.get_segments()
        segments_serializer = SegmentJSON(segments_queryset, many=True)
        return Response(segments_serializer.data)

    def get_single(self, request, pk: int = 1):
        segments_queryset = content_manager.get_segments()
        segments_serializer = SegmentJSON(segments_queryset, many=True)
        return Response(segments_serializer.data)


class SegmentView(APIView):
    def get(self, request, pk: int = None):
        segment_queryset = content_manager.get_segment(pk)
        segment_serializer = SegmentJSON(segment_queryset, many=False)
        return Response(segment_serializer.data)


class MobileOperatorsListView(APIView):
    def get(self, request):
        mobile_operators_queryset = content_manager.get_mobile_operators()
        mobile_operators_serializer = MobileOperatorJSON(mobile_operators_queryset, many=True)
        return Response(mobile_operators_serializer.data)
