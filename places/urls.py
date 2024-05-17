from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views.place_view import PlaceViewSet
from .views.image_upload_view import BulkImageUploadView

router = DefaultRouter()
router.register(r'places', PlaceViewSet, basename='place')
router.register(r'upload', BulkImageUploadView, basename='upload')

urlpatterns = [
    path('', include(router.urls)),
]