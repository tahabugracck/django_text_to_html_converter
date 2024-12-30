from django.contrib import admin
from .models import TextToHTML

@admin.register(TextToHTML)
class TextToHTMLAdmin(admin.ModelAdmin):
    list_display = ('id', 'text_preview', 'created_at')  # Görüntülenen sütunlar
    readonly_fields = ('text', 'html', 'created_at')     # Salt okunur alanlar

    def text_preview(self, obj):
        # Metnin ilk 50 karakterini göster
        return obj.text[:50] + ('...' if len(obj.text) > 50 else '')
    text_preview.short_description = 'Text Preview'
