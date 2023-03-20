from django.shortcuts import render

from van.models import Van, Work_tracking

# Create your views here.
def tracking(request, tracking_id):
    
    van_tracking = Work_tracking.objects.get(tracking_id=tracking_id);
    # van = Van.objects.filter(id=van_tracking.van.id)
    
    return render(request,
                  'van/tracking.html',
                  {'van_tracking': van_tracking})