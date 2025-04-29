from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from .views import VideoDownloadAPIView

urlpatterns = [
    # Render the HTML form when GET request is made
    path('download/', VideoDownloadAPIView.as_view(), name='download_form'),

    # API endpoint to process the video download on POST request
    path('api/download/', VideoDownloadAPIView.as_view(), name='download_video'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)