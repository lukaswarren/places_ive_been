from django.test import TestCase
from django.contrib.auth.models import User
from .models import Place, Visit, Image
from .serializers import PlaceSerializer, VisitSerializer, ImageSerializer

class PlaceModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.place = Place.objects.create(country='USA', city='New York', latLng='40.7128,-74.0060', visible=True, user=self.user)

    def test_place_creation(self):
        self.assertEqual(self.place.country, 'USA')
        self.assertEqual(self.place.city, 'New York')
        self.assertEqual(self.place.latLng, '40.7128,-74.0060')
        self.assertEqual(self.place.visible, True)
        self.assertEqual(self.place.user, self.user)

class VisitModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.place = Place.objects.create(country='USA', city='New York', latLng='40.7128,-74.0060', visible=True, user=self.user)
        self.visit = Visit.objects.create(place=self.place, date='2022-01-01', visitNumber=1, author='John Doe', title='First Visit', content='This is the content of the first visit.')

    def test_visit_creation(self):
        self.assertEqual(self.visit.place, self.place)
        self.assertEqual(self.visit.date, '2022-01-01')
        self.assertEqual(self.visit.visitNumber, 1)
        self.assertEqual(self.visit.author, 'John Doe')
        self.assertEqual(self.visit.title, 'First Visit')
        self.assertEqual(self.visit.content, 'This is the content of the first visit.')

class ImageModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.place = Place.objects.create(country='USA', city='New York', latLng='40.7128,-74.0060', visible=True, user=self.user)
        self.visit = Visit.objects.create(place=self.place, date='2022-01-01', visitNumber=1, author='John Doe', title='First Visit', content='This is the content of the first visit.')
        self.image = Image.objects.create(visit=self.visit, imgID='image1')

    def test_image_creation(self):
        self.assertEqual(self.image.visit, self.visit)
        self.assertEqual(self.image.imgID, 'image1')

class PlaceSerializerTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.place = Place.objects.create(country='USA', city='New York', latLng='40.7128,-74.0060', visible=True, user=self.user)
        self.serializer = PlaceSerializer(instance=self.place)

    def test_contains_expected_fields(self):
        data = self.serializer.data
        self.assertCountEqual(data.keys(), ['country', 'city', 'latLng', 'visible', 'visits'])