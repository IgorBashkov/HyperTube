from django.contrib import admin
from .models import Tag, VideoTag, Video
# Register your models here.


class TagAdmin(admin.ModelAdmin):
    pass


class VideoTagAdmin(admin.ModelAdmin):
    pass


class VideoAdmin(admin.ModelAdmin):
    pass


admin.site.register(Tag, TagAdmin)
admin.site.register(VideoTag, VideoTagAdmin)
admin.site.register(Video, VideoAdmin)
