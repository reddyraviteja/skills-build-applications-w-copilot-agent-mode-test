"""octofit_tracker URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserViewSet, TeamViewSet, ActivityViewSet, LeaderboardViewSet, WorkoutViewSet, api_root
import os
from django.http import JsonResponse



# Custom API root to return API URLs with $CODESPACE_NAME env variable
def custom_api_root(request):
    codespace_name = os.environ.get('CODESPACE_NAME', None)
    scheme = 'https' if request.is_secure() or (codespace_name and request.get_host().startswith(f"{codespace_name}-8000")) else 'http'
    host = request.get_host()
    if codespace_name:
        base_url = f"{scheme}://{codespace_name}-8000.app.github.dev/api/"
    else:
        base_url = f"{scheme}://{host}/api/"
    return JsonResponse({
        'users': base_url + 'users/',
        'teams': base_url + 'teams/',
        'activities': base_url + 'activities/',
        'leaderboard': base_url + 'leaderboard/',
        'workouts': base_url + 'workouts/',
    })

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('', custom_api_root, name='api-root'),
]
