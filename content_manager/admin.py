from django.contrib import admin
from content_manager.models import *


class CityAdmin(admin.ModelAdmin):
    list_display = [field.name for field in City._meta.fields]
    search_fields = ['name']

    class Meta:
        model = City
        verbose_name = 'Город'
        verbose_name_plural = 'Города'

    def __str__(self):
        return self.name


class SegmentAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Segment._meta.fields]
    search_fields = ['name']

    class Meta:
        model = Segment
        verbose_name = 'Сегмент'
        verbose_name_plural = 'Сегменты'

    def __str__(self):
        return self.name


class MobileOperatorAdmin(admin.ModelAdmin):
    list_display = [field.name for field in MobileOperator._meta.fields]
    search_fields = ['name']

    class Meta:
        model = MobileOperator
        verbose_name = 'Оператор связи'
        verbose_name_plural = 'Операторы связи'

    def __str__(self):
        return self.name


admin.site.register(City, CityAdmin)
admin.site.register(Segment, SegmentAdmin)
admin.site.register(MobileOperator, MobileOperatorAdmin)
