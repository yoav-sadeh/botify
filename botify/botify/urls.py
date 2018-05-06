"""botify URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from rest_framework.routers import DefaultRouter
from botify import views
from botify.api.views import SessionEventView

router = DefaultRouter()
router.register(r'session_events', SessionEventView, base_name='user')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('start_session/', views.start_session_view, name='start-session-view'),
    path('session_events/', SessionEventView.as_view, name='session-events'),
]

#urlpatterns += router.urls