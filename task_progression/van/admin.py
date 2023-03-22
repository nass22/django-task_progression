from django.contrib import admin
from .models import Van, Work_tracking, Img_tracking

# Register your models here.
class ImgTrackingInline(admin.TabularInline):
    model = Img_tracking
    extra = 1
    
class WorkTrackingInline(admin.TabularInline):
    # list_display = ('van', 'work_progress_done', 'created_at', 'updated_at')
    model = Work_tracking
    extra = 1

# class VanAdmin(admin.ModelAdmin):
#     list_display = ('customer', 'brand', 'model', 'tracking_id', 'work_progress_percentage', 'finish')
    
class VanAdmin(admin.ModelAdmin):
    list_display = ('customer', 'brand', 'model', 'tracking_id', 'work_progress_percentage', 'finish')
    inlines = [
        WorkTrackingInline, 
        ImgTrackingInline, 
    ]
    
admin.site.register(Van, VanAdmin)

    
# admin.site.register(Van, VanAdmin)
# admin.site.register(Work_tracking, WorkTrackingAdmin)
# admin.site.register(Img_tracking)
