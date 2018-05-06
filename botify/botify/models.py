from django.db import models



class Session(models.Model):
    name = models.CharField(max_length=100)


class SessionEvent(models.Model):

    name = models.CharField(max_length=10)
    session = models.ForeignKey(Session, on_delete=models.CASCADE)
