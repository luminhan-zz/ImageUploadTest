from rest_framework import serializers
from image.models import UploadImage


class UploadImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = UploadImage
        fields = ('pk', 'image',)
