from rest_framework import serializers
from api.models import MyFile

class UploadingSerializer(serializers.ModelSerializer):
    class Meta():
        model = MyFile
        fields = ('original', 'description', 'uploaded_at', 'processed')
