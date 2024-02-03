from django.urls import path

from trip.views import HomeView

urlpatterns = [
    path("", HomeView.as_view(), name="home"),
]
