from django.db import models



class Session(models.Model):
    name = models.CharField(max_length=100)


class SessionEvent(models.Model):

    session_id = models.ForeignKey(Session, on_delete=models.CASCADE)
    name = models.CharField(max_length=10)