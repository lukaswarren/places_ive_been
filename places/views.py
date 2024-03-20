from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from .models import Place, Picture
from .serializers import PlaceSerializer, PictureSerializer


# Create your views here.
class PlacesListView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, *args, **kwargs):
        places = Place.objects.filter(user=request.user.id)
        serializer = PlaceSerializer(places, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        data = {
            'city': request.data.get('city'),
            'country': request.data.get('country'),
            'date': request.data.get('date'),
            'visit_number': request.data.get('visit_number'),
            'user': request.user.id
        }
        serializer = PlaceSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PictureListView (APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, place_id, *args, **kwargs):
        pictures = Picture.objects.filter(place=place_id)
        serializer = PictureSerializer(pictures, many=True);
        return Response(serializer.data, status=status.HTTP_200_OK)