from rest_framework import serializers

from .models import Place, Visit, Image


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = ['imgID']


class VisitSerializer(serializers.ModelSerializer):
    images = ImageSerializer(many=True, read_only=True)

    class Meta:
        model = Visit
        fields = ['date', 'visitNumber', 'author', 'title', 'content', 'images']


class PlaceSerializer(serializers.ModelSerializer):
    visits = VisitSerializer(many=True, read_only=True)

    class Meta:
        model = Place
        fields = ['country', 'city', 'latLng', 'visible', 'visits']

    def create(self, validated_data):
        visits_data = validated_data.pop('visits', [])
        place = Place.objects.create(**validated_data)
        for visit_data in visits_data:
            images_data = visit_data.pop('images', [])
            visit = Visit.objects.create(place=place, **visit_data)
            for image_data in images_data:
                Image.objects.create(visit=visit, **image_data)
        return place
