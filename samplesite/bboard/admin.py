from django.contrib import admin

from .models import Bd


class BbAdmin(admin.ModelAdmin):
    list_display = ('title', 'content', 'price', 'photo', 'published')
    list_display_links = ('title', 'content')
    search_fields = ('title', 'content')


admin.site.register(Bd)