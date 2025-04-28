from django.contrib import admin
from django.utils.html import format_html
from tourism_app.models import City, Attraction, VRVideo
from tourism_app.head_footer_models import HeaderSettings, FooterSettings


@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    list_display = ('name', 'description_short')
    search_fields = ('name', 'description')

    def description_short(self, obj):
        return obj.description[:100] + '...' if len(obj.description) > 100 else obj.description

    description_short.short_description = 'Qisqa tavsif'


@admin.register(Attraction)
class AttractionAdmin(admin.ModelAdmin):
    list_display = ('name', 'city', 'image_preview')
    list_filter = ('city',)
    readonly_fields = ('image_preview',)

    def image_preview(self, obj):
        if obj.image:
            return format_html('<img src="{}" class="image-preview" />', obj.image.url)
        return "Rasm yo'q"

    image_preview.short_description = 'Rasm'


@admin.register(VRVideo)
class VRVideoAdmin(admin.ModelAdmin):
    list_display = ('title', 'city', 'video_embed', 'created_at')
    readonly_fields = ('video_embed',)

    def video_embed(self, obj):
        if obj.embed_url:
            return format_html(
                '<div class="video-preview">'
                '<iframe src="{}" frameborder="0" allowfullscreen></iframe>'
                '</div>',
                obj.embed_url
            )
        return "Video yo'q"

    video_embed.short_description = 'Video'


@admin.register(HeaderSettings)
class HeaderSettingsAdmin(admin.ModelAdmin):
    list_display = ('title', 'banner_preview')
    readonly_fields = ('banner_preview',)

    def has_add_permission(self, request):
        return not HeaderSettings.objects.exists()

    def banner_preview(self, obj):
        if obj.banner_image:
            return format_html('<img src="{}" class="image-preview" />', obj.banner_image.url)
        return "Banner yo'q"

    banner_preview.short_description = 'Banner'


@admin.register(FooterSettings)
class FooterSettingsAdmin(admin.ModelAdmin):
    list_display = ('phone', 'email', 'social_links')

    def has_add_permission(self, request):
        return not FooterSettings.objects.exists()

    def social_links(self, obj):
        links = []
        if obj.telegram_url:
            links.append(f'<a href="{obj.telegram_url}" target="_blank">Telegram</a>')
        if obj.instagram_url:
            links.append(f'<a href="{obj.instagram_url}" target="_blank">Instagram</a>')
        if obj.facebook_url:
            links.append(f'<a href="{obj.facebook_url}" target="_blank">Facebook</a>')
        if obj.youtube_url:
            links.append(f'<a href="{obj.youtube_url}" target="_blank">YouTube</a>')
        return format_html(' | '.join(links)) if links else "Ijtimoiy tarmoqlar yo'q"

    social_links.short_description = 'Ijtimoiy tarmoqlar'