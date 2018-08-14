from rest_framework import viewsets, authentication, permissions
from rest_framework.views import APIView

from botify.api.serializers import SessionEventSerializer, DOMElementEventSerializer, SessionSerializer
from botify.models import SessionEvent, DOMElementEvent, Session


class SessionEventView(APIView):
    #serializer_class = SessionEventSerializer

    #permission_classes = (permissions.IsAdminUser,)
    def get_queryset(self):
        return SessionEvent.objects.all()

    def post(self, request, format=None):
        pass

class DOMElementEventViewSet(viewsets.ModelViewSet):
    queryset = DOMElementEvent.objects.all()
    serializer_class = DOMElementEventSerializer

class SessionViewSet(viewsets.ModelViewSet):
    queryset = Session.objects.all()
    serializer_class = SessionSerializer
