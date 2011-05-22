from django.db import models

class Poll(models.Model):
  question = models.CharField(max_length=255)
  creation_date = models.DateTimeField(auto_now_add=True)
  modification_date = models.DateTimeField(auto_now=True)
  def __str__(self):
    return self.question
  pass

class Choice(models.Model):
  poll = models.ForeignKey(Poll)
  choice = models.CharField(max_length=255)
  votes = models.IntegerField()
  def __str__(self):
    return self.choice
  pass
