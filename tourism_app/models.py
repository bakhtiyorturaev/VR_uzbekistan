from django.db import models
from django.utils.translation import gettext_lazy as _
from urllib.parse import urlparse, parse_qs

class City(models.Model):
    name = models.CharField(max_length=100, verbose_name=_('Shahar nomi'))
    description = models.TextField(verbose_name=_('Tavsif'))

    class Meta:
        verbose_name = _('Shahar')
        verbose_name_plural = _('Shaharlar')
        ordering = ['name']

    def __str__(self):
        return self.name

class Attraction(models.Model):
    city = models.ForeignKey(City, on_delete=models.CASCADE, related_name='attractions', verbose_name=_('Shahar'))
    name = models.CharField(max_length=100, verbose_name=_('Joy nomi'))
    image = models.ImageField(upload_to='attractions/', verbose_name=_('Rasm'))

    class Meta:
        verbose_name = _('Diqqatga Sazovor Joy')
        verbose_name_plural = _(' Diqqatga Sazovor Joylar')
        ordering = ['city','name']

    def __str__(self):
        return f'{self.city} - {self.name}'

class VRVideo(models.Model):
    city = models.ForeignKey(City, on_delete=models.CASCADE, related_name='videos')
    title = models.CharField(max_length=200, verbose_name=_('Video sarlavhasi'))
    video_url = models.URLField(verbose_name=_('YouTube URL'))
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = _('VR Video')
        verbose_name_plural = _('VR Videolar')
        # ordering = ['city','title']

    def __str__(self):
        return f'{self.city} - {self.title}'

    @property
    def embed_url(self):
        """Improved YouTube embed URL generator that handles multiple URL formats"""
        url = urlparse(self.video_url)

        # Standard YouTube URL (https://www.youtube.com/watch?v=ID)
        if 'youtube.com' in url.netloc:
            video_id = parse_qs(url.query).get('v', [''])[0]

        # Short YouTube URL (https://youtu.be/ID)
        elif 'youtu.be' in url.netloc:
            video_id = url.path[1:]

        # YouTube mobile URL (https://m.youtube.com/watch?v=ID)
        elif 'm.youtube.com' in url.netloc:
            video_id = parse_qs(url.query).get('v', [''])[0]

        # YouTube-nocookie.com URL (for privacy-enhanced mode)
        elif 'youtube-nocookie.com' in url.netloc:
            video_id = parse_qs(url.query).get('v', [''])[0]

        else:
            return None

        if not video_id:
            return None

        # Force HTTPS for the embed URL
        return f"https://www.youtube-nocookie.com/embed/{video_id}?rel=0"


