from rest_framework import viewsets, authentication, permissions
from rest_framework.views import APIView

from botify.api.serializers import SessionEventSerializer
from botify.models import SessionEvent


class SessionEventView(APIView):
    #serializer_class = SessionEventSerializer

    #permission_classes = (permissions.IsAdminUser,)
    def get_queryset(self):
        return SessionEvent.objects.all()

    def post(self, request, format=None):
        pass
