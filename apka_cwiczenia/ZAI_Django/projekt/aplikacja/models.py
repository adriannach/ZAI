from django.db import models

class Questions(models.Model):
    question_text = models.CharField(max_length=300)
    pub_date = models.DateField()

class Choice(models.Model):
    question = models.ForeignKey(Questions, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=250)
    vote = models.IntegerField(default=0)

# Create your models here.
