from django.contrib import admin
from .models.models import Comment
from .models.artitem import Tag, ArtItem
from .models.user import User


class UserAdmin(admin.ModelAdmin):
    list_display = ['username', 'id', 'name', 'surname', 'email', 'created_at', 'updated_at']

class TagAdmin(admin.ModelAdmin):
    list_display =  ['tagname', 'id', 'description', 'created_at', 'updated_at']

class CommentAdmin(admin.ModelAdmin):
    list_display = ['body', 'id', 'commented_by', 'commented_on', 'created_at']

class ArtItemAdmin(admin.ModelAdmin):
    list_display = ['title', 'id', 'description', 'owner', 'artitem_image']

admin.site.register(User, UserAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(ArtItem, ArtItemAdmin)