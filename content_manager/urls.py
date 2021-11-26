from django.urls import path
from .views import CitiesListView, SegmentsListView, CityView, SegmentView, MobileOperatorsListView

urlpatterns = [
    path('cities/', CitiesListView.as_view()),
    path('cities/<int:pk>', CityView.as_view()),
    path('segments/', SegmentsListView.as_view()),
    path('segments/<int:pk>', SegmentView.as_view()),
    path('mobile_operators/', MobileOperatorsListView.as_view())
]
