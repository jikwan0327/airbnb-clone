from itertools import count
from django.db import models
from core import models as core_models

class Conversation(core_models.TimeStampedModel):

    participants = models.ManyToManyField("users.User", blank=True)

    def __str__(self):
        usernames = []
        for user in self.participants.all():
            usernames.append(user.username)
        return ", ".join(usernames) #채팅방 이름을 채팅방에 있는 이름으로 출력(예 tom과 jerry가 대화방에 있으면 대화방 이름은 tom, jerry임)

    def count_messages(self): # 메세지의 개수
        return self.messages.count() 
    count_messages.short_description = "Number of Messages" # count_messages인 제목을 Number of Messages로 바꿈

    def count_participants(self): # 참가자 수 
        return self.participants.count() 
    count_participants.short_description = "Number of Participants"

class Message(core_models.TimeStampedModel):

    message = models.TextField()
    user = models.ForeignKey("users.User", related_name="messages",on_delete=models.CASCADE)
    conversation = models.ForeignKey("Conversation", related_name="messages", on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.user} says: {self.message}'