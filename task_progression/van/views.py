from django.shortcuts import render

from van.models import Van, Work_tracking

# Create your views here.


def tracking(request, tracking_id):

    van = Van.objects.get(tracking_id=tracking_id)
    work_tracking = Work_tracking.objects.filter(van=van).order_by('-created_at')
    # van = Van.objects.filter(id=van_tracking.van.id)

    return render(request,
                  'van/tracking.html',
                  {'van': van,
                   'work_tracking': work_tracking})
