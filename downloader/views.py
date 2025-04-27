from django.shortcuts import render
from django.http import JsonResponse, FileResponse
from rest_framework.views import APIView
import yt_dlp
import uuid
import json

class VideoDownloadAPIView(APIView):
    def get(self, request):
        return render(request, 'home.html')

    def post(self, request):
        try:
            data = json.loads(request.body)
            url = data.get('url')

            if not url:
                return JsonResponse({'error': 'Video URL is required'}, status=400)

            file_id = str(uuid.uuid4())
            output_file = f"media/{file_id}.mp4"

            ydl_opts = {
                'format': 'best',
                'outtmpl': output_file,
                'quiet': True,
            }

            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                ydl.download([url])

            return FileResponse(open(output_file, 'rb'), as_attachment=True, filename=f"{file_id}.mp4")

        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)
