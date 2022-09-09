from django.db import models

class TimeStampedModel(models.Model):

    """Time Stamped Model"""
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta: #기타 사항
        abstract = True #모델이지만 데이터베이스에 나타나지 않는 모델