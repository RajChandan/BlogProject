from django.contrib import admin
from .models import  Post,Comments
# Register your models here.
class PostAdmin(admin.ModelAdmin):
    list_display=['title','slug','author','body','publish','created','updated','status']
    list_filter=('status','author')
    search_fields=('title','body')
    ordering=('status','publish')
    prepopulated_fields={'slug':('title',)}
admin.site.register(Post,PostAdmin)


class CommentAdmin(admin.ModelAdmin):
    list_display=('name','email','post','body','created','updated','active')
    list_filter=('active','created','updated')
    search_field=('name','email','body')

admin.site.register(Comments,CommentAdmin)