"""Posts admin clasess"""

# Django
from django.contrib import admin


# Models
from posts.models import Post

# Register Post

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('pk','user', 'title', 'photo')
    list_display_links = ('pk','user')
    list_editable = ('title', 'photo')

    list_filter = ('created', 'modified')

    fieldsets = (
        ('Posts', {
            'fields': (
                ('user', 'title', 'photo'),
            ),
        }),
    )

    readonly_fields = ('created', 'modified')