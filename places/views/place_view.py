from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from ..models import Place
from ..serializers import PlaceSerializer


class PlaceViewSet(viewsets.ModelViewSet):
    serializer_class = PlaceSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        # Returns only locations associated with the authenticated user
        return Place.objects.filter(user=self.request.user)

