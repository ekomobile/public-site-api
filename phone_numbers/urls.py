from django.urls import path
from .views import PhoneNumbersListView, PhoneNumberView


urlpatterns = [
    path('', PhoneNumbersListView.as_view()),
    path('<int:pk>', PhoneNumberView.as_view())
]
