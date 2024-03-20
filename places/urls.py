from django.urls import path, include
from .views import (
    PlacesListView,
)

urlpatterns = [
    path('places', PlacesListView.as_view()),
]