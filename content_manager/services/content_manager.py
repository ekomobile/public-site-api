from content_manager.models import City, Segment, MobileOperator


def get_cities():
    return City.objects.all().order_by('id')


def get_city(pk: int):
    return City.objects.get(id=pk)


def get_segments():
    return Segment.objects.all().order_by('id')


def get_segment(pk: int):
    return Segment.objects.get(id=pk)


def get_mobile_operators():
    return MobileOperator.objects.all().order_by('id')
