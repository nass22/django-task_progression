from django.shortcuts import render
from van.models import Van, Work_tracking, Img_tracking, Work_requested

# Create your views here.


def tracking(request, tracking_id):

    van = Van.objects.get(tracking_id=tracking_id)
    work_requested = Work_requested.objects.filter(van=van)
    work_tracking = Work_tracking.objects.filter(van=van).order_by('-created_at')
    img_tracking = Img_tracking.objects.filter(van=van).order_by('-created_at')

    return render(request,
                  'van/tracking.html',
                  {'van': van,
                   'work_requested': work_requested,
                   'work_tracking': work_tracking,
                   'img_tracking': img_tracking})
