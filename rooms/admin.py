from django.contrib import admin
from . import models

@admin.register(models.RoomType, models.Facility, models.Amenity, models.HouseRule) #필드에 값을 추가할 수 있게 해줌
class ItemAdmin(admin.ModelAdmin):

    """ Item Admin Definition """

    list_display = (
        "name",
        "used_by"
    )

    def used_by(self, obj):
        return obj.rooms.count()

    pass

@admin.register(models.Room)
class RoomAdmin(admin.ModelAdmin):

    """ Room Admin Definition """

    fieldsets = ( #보이는 필드 구분
        (
            "Basic Info",
            {"fields": ("name", "description", "country", "address", "price")}
        ),
        (
            "Times",
            {"fields": ("check_in", "check_out", "instant_book")}
        ),
        ("Spaces", {"fields": ("guests", "beds", "bedrooms", "baths") }),
        (
            "More About the Space",
            {
                "classes": ('collapse',), #숨기기와 보이기 기능을 만들어줌
                "fields": ("amenities", "facilities", "house_rules")
            }
        ),
        (
            "Last Details",
            {"fields": ("host",)}
        )
    )

    list_display = (
        "name",
        "country",
        "city",
        "price",
        "address",
        "guests",
        "beds",
        "bedrooms",
        "baths",
        "check_in",
        "check_out",
        "instant_book",
        "count_amenities",
        "count_photos",
        "total_rating",
    )

    ordering = ('name', 'price', 'bedrooms')

    list_filter = (
        "instant_book",
        "host__superhost",
        "room_type",
        "amenities",
        "facilities",
        "house_rules",
        "city",
        "country",
    )

    search_fields = ("^city", "^host__username")

    filter_horizontal = (
        "amenities",
        "facilities",
        "house_rules",
    )

    def count_amenities(self, obj):
        return obj.amenities.count()

    def count_photos(self, obj):
        return obj.photos.count()

@admin.register(models.Photo)
class PhotoAdmin(admin.ModelAdmin):

    """"""
    pass 