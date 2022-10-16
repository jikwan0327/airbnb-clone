from django.contrib import admin
from . import models 

# Register your models here.
@admin.register(models.List)
class ListAdmin(admin.ModelAdmin):

    list_display = (
        "name",
        "user",
        "count_rooms"
    )

    search_fields = ("name", ) #검색 필터 name에 해당하는 글자 중 하나라도 있으면 검색됨

    filter_horizontal = ("rooms", )