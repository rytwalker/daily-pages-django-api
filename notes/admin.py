from django.contrib import admin
from .models import Note, UserNote


class NoteAdmin(admin.ModelAdmin):
    readonly_fields = ('created_at', 'updated_at')


admin.site.register(Note, NoteAdmin)
admin.site.register(UserNote)
