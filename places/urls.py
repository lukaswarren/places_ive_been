from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views.login import LoginLogout, SessionView, WhoAmIView
from .views.place_view import PlaceViewSet
from .views.image_upload import ImageUploadView

router = DefaultRouter()
router.register(r'places', PlaceViewSet, basename='place')


urlpatterns = [
    path('', include(router.urls)),
    path('upload/', ImageUploadView.as_view(), name='image-upload'),
    path('login/', LoginLogout.login_view, name='login'),
    path('logout/', LoginLogout.logout_view, name='logout'),
    path('whoami/', WhoAmIView.as_view(), name='whoami'),
    path('csrf/', LoginLogout.get_csrf, name='csrf'),
]