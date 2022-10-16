from django.db import models
from django.utils import timezone #시간 관련
from core import models as core_models


class Reservation(core_models.TimeStampedModel):

    """ Reservation Model Definition """

    STATUS_PENDING = 'pending'
    STATUS_CONFIRMED = "confirmed"
    STATUS_CANCELED = "canceled"

    STATUS_CHOICES = (
        (STATUS_PENDING, "Pending"),
        (STATUS_CONFIRMED, "Confirmed"),
        (STATUS_PENDING, "Canceled"),
     )

    status = models.CharField(max_length=12, choices=STATUS_CHOICES, default=STATUS_PENDING)
    check_in = models.DateField()
    check_out = models.DateField()
    guest = models.ForeignKey("users.User", on_delete=models.CASCADE)
    room = models.ForeignKey("rooms.Room", on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.room} - {self.check_in}'

    def in_progress(self): # 오늘 방 예약 여부를 확인하는 함수
        now = timezone.now().date()
        return now > self.check_in and now < self.check_out 

    in_progress.boolean = True #in_progress 진행 여부를 False, True 글자 대신 모양으로 가져옴

    def is_finished(self): # 오늘부터 예약 가능 여부
        now = timezone.now().date()
        return now > self.check_out

    is_finished.boolean = True