from django.contrib import admin
from .models import Van, Work_tracking, Img_tracking

# Register your models here.

class VanAdmin(admin.ModelAdmin):
    list_display = ('customer', 'brand', 'model', 'tracking_id', 'work_progress_percentage', 'finish')
    
class WorkTrackingAdmin(admin.ModelAdmin):
    list_display = ('van', 'work_progress_done', 'created_at', 'updated_at')

    
admin.site.register(Van, VanAdmin)
admin.site.register(Work_tracking, WorkTrackingAdmin)
admin.site.register(Img_tracking)
