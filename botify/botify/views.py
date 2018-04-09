from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render

from .models import Session, SessionEvent


def index(request):
    """
    View function for home page of site.
    """
    # Generate counts of some of the main objects
    num_sessions = Session.objects.all().count()
    num_events = SessionEvent.objects.all().count()
    # Available books (status = 'a')

    # Render the HTML template index.html with the data in the context variable
    return render(
        request,
        'index.html',
        context={'num_sessions': num_sessions, 'num_events': num_events},
    )