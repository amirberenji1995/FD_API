from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response
from rest_framework import status
from api.serializers import UploadingSerializer
from api.models import MyFile

from PIL import Image
from scripts.test import face_detector

from django.forms.models import model_to_dict

## add stands for the address of the parent Django folder of the project
add = '/home/amir/venvs/new ones/FD_api/FD_api/face_detect_api/'

class MyFileView(APIView):
    parser_classes = (MultiPartParser,)
    def post(self, request, format = None):
        file_serializer = UploadingSerializer(data = request.data)
        if file_serializer.is_valid():
            file_serializer.save()
            image = face_detector(add, file_serializer.data['original'])

            File = MyFile.objects.latest('uploaded_at')
            File.processed = image
            File.save()

            File = MyFile.objects.latest('uploaded_at')
            result = UploadingSerializer(File)
            return Response(result.data, status = status.HTTP_201_CREATED)
        else:
            return Response(file_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
