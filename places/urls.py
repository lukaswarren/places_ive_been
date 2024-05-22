from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views.place_view import PlaceViewSet
from .views.image_upload_view import ImageUploadView

router = DefaultRouter()
router.register(r'places', PlaceViewSet, basename='place')


urlpatterns = [
    path('', include(router.urls)),
    path('upload/', ImageUploadView.as_view(), name='image-upload'),
]