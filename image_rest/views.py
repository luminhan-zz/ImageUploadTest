from rest_framework import viewsets
from image_rest.serializers import UploadImageSerializer
from image.models import UploadImage


class UploadImageViewSet(viewsets.ModelViewSet):
    queryset = UploadImage.objects.all()
    serializer_class = UploadImageSerializer

