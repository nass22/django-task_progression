from django.contrib import admin
from .models import Van, Work_tracking, Img_tracking

# Register your models here.
class WorkTrackingAdmin(admin.ModelAdmin):
    list_display = ('van', 'tracking_id', 'work_progress_percentage', 'finish')
    
admin.site.register(Van)
admin.site.register(Work_tracking, WorkTrackingAdmin)
admin.site.register(Img_tracking)
