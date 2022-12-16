from django.contrib import admin
from .models import Comment, DesignInfo, Likes
# Register your models here.

admin.site.register(Comment)
admin.site.register(DesignInfo)
admin.site.register(Likes)
