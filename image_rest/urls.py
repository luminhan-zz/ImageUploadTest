from django.conf.urls import url, include
from rest_framework import routers
from image_rest.views import UploadImageViewSet

router = routers.DefaultRouter()
router.register('images', UploadImageViewSet, 'images')

urlpatterns = [
    url(r'^', include(router.urls))
]
