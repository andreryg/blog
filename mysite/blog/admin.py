from django.contrib import admin
from .models import Post

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'image', 'status', 'created_on')
    list_filter = ('status', 'slug')
    search_fields = ['title', 'content']
    prepopulated_fields = {'slug': ('title',)}


admin.site.register(Post, PostAdmin)