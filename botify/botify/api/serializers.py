from rest_framework import serializers

class SessionEventSerializer(serializers.ListSerializer):

    class Meta:
        fields = ('name','session', )