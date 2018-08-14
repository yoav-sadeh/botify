from django.db import models



class Session(models.Model):
    name = models.CharField(max_length=100)


class SessionEvent(models.Model):

    name = models.CharField(max_length=10)
    session = models.ForeignKey(Session, on_delete=models.CASCADE)

class DOMElementEvent(models.Model):
    CREATE = 'CR'
    UPDATE = 'UP'
    DELETE = 'DE'

    EVENT_TYPES = (
        (CREATE, 'Create'),
        (UPDATE, 'Update'),
        (DELETE, 'Delete'),
    )
    session = models.ForeignKey(Session, on_delete=models.CASCADE)
    event_type = models.CharField(max_length=2, choices=EVENT_TYPES, default=CREATE) #EventType.CREATE,
    path= models.TextField() #'/HTML[1]/BODY[1]/DIV[1]/DIV[3]/FORM[1]/DIV[2]',
    attributes= models.TextField() #{"value": "יותר מזל משכל","aria-label": "יותר מזל משכל","name": "btnI","type": "submit","jsaction": "sf.lck"}
