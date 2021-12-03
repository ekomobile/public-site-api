from .services.phone_numbers_collector import DealersAPI
from .services.phone_filter import PhoneNumbersFilter
from typing import List
from rest_framework.response import Response
from rest_framework.views import APIView


class PhoneNumbersListView(APIView):
    def get(self, request):
        phone_type: int = int(request.GET.get('phone_type', 1))
        mobile_operator: int = int(request.GET.get('mobile_operator', 1))
        include_numbers: List[str] = request.GET.getlist('include_numbers', [])
        exclude_numbers: List[str] = request.GET.getlist('exclude_numbers', [])
        phone_number_mask: List[any] = request.GET.get('phone_number_mask', '')
        phone_number_mask_strict: bool = request.GET.get('phone_number_mask_strict', False)
        print(phone_number_mask)

        include_numbers_n = []
        for number in include_numbers:
            include_numbers_n.append(int(number))

        exclude_numbers_n = []
        for number in exclude_numbers:
            exclude_numbers_n.append(int(number))

        raw_phone_numbers_list = DealersAPI().get_phone_numbers_list()
        filtered_list = PhoneNumbersFilter(phone_type, mobile_operator, include_numbers_n, exclude_numbers_n,
                                           phone_number_mask,phone_number_mask_strict)\
            .get_filtered_phone_numbers_list(raw_phone_numbers_list)
        return Response(filtered_list, status=200)


class PhoneNumberView(APIView):
    def get(self, request, pk: int):
        return Response(f"ok: {pk}", status=200)
