# views.py
from django.http import JsonResponse
from django.conf import settings
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.parsers import MultiPartParser, FormParser
import os
from datetime import datetime
from django.core.files.storage import FileSystemStorage

class ImageUploadView(APIView):
    permission_classes = [IsAuthenticated]
    parser_classes = (MultiPartParser, FormParser,)

    def post(self, request, *args, **kwargs):
        image_file = request.FILES.get('image')
        country = request.data.get('country')
        city = request.data.get('city')
        date = request.data.get('date')  # Expecting date in YYYY-MM-DD format

        if image_file and country and city and date:
            # Format the date and construct the directory path
            date_formatted = datetime.strptime(date, '%Y-%m-%d').strftime('%Y%m%d')
            user_id = request.user.id
            directory_path = os.path.join(settings.MEDIA_ROOT,  str(user_id), country, city, date_formatted)

            if not os.path.exists(directory_path):
                os.makedirs(directory_path)
            
            fs = FileSystemStorage(location=directory_path)
            filename = fs.save(image_file.name, image_file)
            file_url = fs.url(filename)
            
            return JsonResponse({'imgID': filename, 'url': file_url}, status=201)
        else:
            return JsonResponse({'error': 'Missing required fields or image file'}, status=400)
