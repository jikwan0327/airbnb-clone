from tabnanny import verbose
from django.db import models
from django_countries.fields import CountryField
from core import models as core_models
 
class AbstractItem(core_models.TimeStampedModel):

    """Abstract Item"""

    name = models.CharField(max_length=80)
    class Meta:
        abstract = True

    def __str__(self):
         return self.name
 
class RoomType(AbstractItem):

    """ RoomType Object Definition"""

    class Meta:
        verbose_name = "Room Type"
        ordering = ['name'] #이름 순으로 정렬

class Amenity(AbstractItem): #편의 시설

    """ Amenity Object Definition"""

    class Meta:
        verbose_name_plural = "Amenities"


class Facility(AbstractItem):

    """ Facility Model Definiton"""

    class Meta:
        verbose_name_plural = "Facilities"


class HouseRule(AbstractItem):

    """ HouseRule Model  Definition """

    class Meta:
        verbose_name = "House Rule"

class Photo(core_models.TimeStampedModel):

    """ Photo Model Definition """

    caption = models.CharField(max_length=80) #이미지 설명
    file = models.ImageField()
    room = models.ForeignKey("Room", on_delete=models.CASCADE)

    def __str__(self):
        return self.caption

class Room(core_models.TimeStampedModel):

    """Room Model Definition"""

    name = models.CharField(max_length=140) #required 즉 필수 입력사항이기 때문에 null이나 blank를 주지 않음
    description = models.TextField()
    country = CountryField()
    city = models.CharField(max_length=80)
    price = models.IntegerField()
    address = models.CharField(max_length=140)
    guests = models.IntegerField()
    beds = models.IntegerField()
    bedrooms = models.IntegerField()
    baths = models.IntegerField()
    check_in = models.TimeField()
    check_out = models.TimeField()
    instant_book = models.BooleanField(default=False)
    host = models.ForeignKey("users.User", related_name="rooms", on_delete=models.CASCADE) #ForeignKey : 다른 어플리케이션과 연결시킴
    room_type = models.ForeignKey("RoomType", related_name="room_types" ,on_delete=models.SET_NULL, null=True) #방의 한가지 유형만 선택하게 함
    amenities = models.ManyToManyField("Amenity",related_name="rooms", blank=True)
    facilities = models.ManyToManyField("Facility", related_name="rooms", blank=True)
    house_rules = models.ManyToManyField("HouseRule", related_name="rooms", blank=True)

    def __str__(self):
        return self.name #파란색 밑에 이름을 방이름으로 변경(원래는 Rooms Object)로 뜸