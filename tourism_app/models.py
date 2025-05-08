from django.db import models
from django.utils.translation import gettext_lazy as _
from urllib.parse import urlparse, parse_qs
import re


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

    def __str__(self):
        return f'{self.city} - {self.title}'


    @property
    def embed_url(self):
        """Generate proper YouTube embed URL from various YouTube URL formats"""
        if not self.video_url:
            return None

        # Regular expression to extract video ID from various YouTube URL formats
        regex = r'(?:youtube\.com\/(?:[^\/]+\/.+\/|(?:v|e(?:mbed)?)\/|youtu\.be\/|youtube-nocookie\.com\/(?:embed\/|v\/)?)([^"&?\/\s]{11})'
        match = re.search(regex, self.video_url)

        if match:
            video_id = match.group(1)
            return f"https://www.youtube-nocookie.com/embed/{video_id}?rel=0&modestbranding=1"
        return None


