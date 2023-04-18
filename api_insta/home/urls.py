from .views import getRoutes,getStats,getStat
from django.urls import path

urlpatterns = [
    path('', getRoutes),
    path('stats/',getStats),
    path('stats/<int:stat_id>/',getStat),
]