from django.contrib import admin
from .models import Post

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_date')
    list_filter = ('created_date',)
    search_fields = ('title', 'content')
    date_hierarchy = 'created_date'