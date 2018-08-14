from rest_framework import serializers

from botify.models import DOMElementEvent, Session


class SessionEventSerializer(serializers.ListSerializer):

    class Meta:
        fields = ('name','session', )

class DOMElementEventSerializer(serializers.ModelSerializer):

    class Meta:
        model = DOMElementEvent
        fields = ('id', 'session','event_type', 'path', 'attributes',)

class SessionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Session
        fields = ('name', 'id',)