import os
import uuid
import yt_dlp
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
import mimetypes
import json


def home(request):
    """Render home page with video download form"""
    return render(request, 'youtube_downloader/home.html')


@csrf_exempt
def download_video(request):
    """Handle YouTube video download requests"""
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            video_url = data.get('video_url')
            format_type = data.get('format_type', 'video')  # Default to video format

            if not video_url:
                return JsonResponse({'error': 'Video URL is required'}, status=400)

            # Ensure download directory exists
            if not os.path.exists(settings.DOWNLOADS_ROOT):
                os.makedirs(settings.DOWNLOADS_ROOT)

            # Generate a unique filename
            unique_id = str(uuid.uuid4())

            # Download options based on format selection
            if format_type == 'audio':
                # Audio (MP3) options
                output_filename = f"{unique_id}.mp3"
                download_options = {
                    'format': 'bestaudio/best',
                    'postprocessors': [{
                        'key': 'FFmpegExtractAudio',
                        'preferredcodec': 'mp3',
                        'preferredquality': '192',
                    }],
                    'outtmpl': os.path.join(settings.DOWNLOADS_ROOT, output_filename),
                }
            else:
                # Video (MP4) options
                output_filename = f"{unique_id}.mp4"
                download_options = {
                    'format': 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best',
                    'outtmpl': os.path.join(settings.DOWNLOADS_ROOT, output_filename),
                }

            # Extract video information
            with yt_dlp.YoutubeDL() as ydl:
                info = ydl.extract_info(video_url, download=False)
                video_info = {
                    'title': info.get('title', 'Unknown Title'),
                    'thumbnail': info.get('thumbnail'),
                    'duration': info.get('duration'),
                    'description': info.get('description'),
                    'channel': info.get('uploader'),
                }

            # Download the video
            with yt_dlp.YoutubeDL(download_options) as ydl:
                ydl.download([video_url])

            # Prepare download URL
            relative_path = os.path.join('downloads', output_filename)
            download_url = f"/media/{relative_path}"

            # Return information about the video and download link
            return JsonResponse({
                'success': True,
                'download_url': download_url,
                'video_info': video_info,
                'format': format_type,
                'filename': video_info['title'] + ('.mp3' if format_type == 'audio' else '.mp4')
            })

        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)

    return JsonResponse({'error': 'Method not allowed'}, status=405)
