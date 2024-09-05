from datetime import timezone

from django.shortcuts import render
from django.utils import timezone

from creator.video_creator_script import create_video
from creator.models import Video


def index(request):
    text = request.GET.get('text')
    if text:
        create_video(text)
        q = Video(text=text, pub_date=timezone.now(), file=f'media/{text[:15]}.mp4'.replace(' ', '_'))
        q.save()
    all_files = Video.objects.all()
    context = {
        "all_files": all_files,
    }
    return render(request, 'index.html', context=context)
