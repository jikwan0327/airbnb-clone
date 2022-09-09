from django.contrib import admin
from . import models

@admin.register(models.RoomType, models.Facility, models.Amenity, models.HouseRule) #필드에 값을 추가할 수 있게 해줌
class ItemAdmin(admin.ModelAdmin):

    """ Item Admin Definition """

    pass

@admin.register(models.Room)
class RoomAdmin(admin.ModelAdmin):

    """ Room Admin Definition """

    pass

@admin.register(models.Photo)
class PhotoAdmin(admin.ModelAdmin):

    """"""
    pass