import datetime

from django.db import models
from django.utils import timezone

# Create your models here.
class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date published")
    def __str__(self):
        return self.question_text
    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now #Question 생성 날자가 미래로 넘어가지 않도록 현재 날짜를 두고 최근 기준을 하루로 둠


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE) #외래키(Question table 참조)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    def __str__(self):
        return self.choice_text
