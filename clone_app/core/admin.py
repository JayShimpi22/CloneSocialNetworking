from django.contrib import admin
from core.models import *
# Register your models here.
@admin.register(PostModel)
class PostAdmin(admin.ModelAdmin):
    model = PostModel
    list_display = ('text','image','user','created_on','updated_on')

@admin.register(CommentModel)
class CommentAdmin(admin.ModelAdmin):
    model = CommentModel
    list_display = ('text','post','user','commented_on','updated_on')

@admin.register(LikeModel)
class LikeAdmin(admin.ModelAdmin):
    model = LikeModel
    list_display = ('post','user','liked_on','updated_on')
    
@admin.register(FollowerModel)
class FollowerAdmin(admin.ModelAdmin):
    model = FollowerModel
    list_display = ('user','followed','followed_on','updated_on')

    
@admin.register(SavedPost)
class SavedpostAdmin(admin.ModelAdmin):
    model = SavedPost
    list_display = ('post','user','saved_on',)

