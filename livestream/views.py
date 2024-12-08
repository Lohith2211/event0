from django.shortcuts import render, redirect
from .models import LiveStream
from django.utils import timezone
from django.shortcuts import render, get_object_or_404


def create_stream(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        stream_url = request.POST.get('stream_url')
        start_time = request.POST.get('start_time')
        end_time = request.POST.get('end_time')

        LiveStream.objects.create(
            title=title,
            description=description,
            stream_url=stream_url,
            start_time=start_time,
            end_time=end_time,
            is_live=True  # You may want to toggle this based on the actual streaming status
        )
        return redirect('stream_list')

    return render(request, 'create_stream.html')


def stream_list(request):
    streams = LiveStream.objects.all()
    return render(request, 'stream_list.html', {'streams': streams})

#
# def live_stream_view(request, stream_id):
#     stream = get_object_or_404(LiveStream, id=stream_id)
#     return render(request, 'livestream.html', {'stream': stream})


# Create your views here.
