from django.db import models
from django.utils.translation import gettext_lazy as _

class HeaderSettings(models.Model):
    banner_image = models.ImageField(
        _("Banner rasmi"),
        upload_to='header/',
        default='header/default_banner.jpg'
    )
    title = models.CharField(
        _("Sarlavha"),
        max_length=100,
        default="O'ZBEKISTONGA XUSH KELIBSIZ"
    )
    subtitle = models.CharField(
        _("Pastki sarlavha"),
        max_length=200,
        default="VR sayohatlar orqali O'zbekistonning go'zal turistik joylariga virtual tashrif buyuring"
    )
    is_active = models.BooleanField(_("Faol"), default=True)

    class Meta:
        verbose_name = _("Header sozlamasi")
        verbose_name_plural = _("Header sozlamalari")

    def __str__(self):
        return f"Header sozlamalari (ID: {self.id})"

    def save(self, *args, **kwargs):
        # Faqat bitta faol header bo'lishi uchun
        if self.is_active:
            HeaderSettings.objects.exclude(pk=self.pk).update(is_active=False)
        super().save(*args, **kwargs)


class FooterSettings(models.Model):
    description = models.TextField(
        _("Tavsif"),
        default="Virtual reallik texnologiyalari orqali O'zbekistonning noyob diqqatga sazovor joylarini dunyoga tanitamiz."
    )
    phone = models.CharField(
        _("Telefon raqam"),
        max_length=20,
    )
    email = models.EmailField(
        _("Elektron pochta"),
    )
    telegram_url = models.URLField(
        _("Telegram havolasi"),
        blank=True,
        default="#"
    )
    instagram_url = models.URLField(
        _("Instagram havolasi"),
        blank=True,
        default="#"
    )
    facebook_url = models.URLField(
        _("Facebook havolasi"),
        blank=True,
        default="#"
    )
    youtube_url = models.URLField(
        _("YouTube havolasi"),
        blank=True,
        default="#"
    )
    copyright_text = models.CharField(
        _("Copyright matni"),
        max_length=200,
        default="© 2025 O'zbekiston VR Sayohatlar. Barcha huquqlar himoyalangan."
    )
    is_active = models.BooleanField(
        _("Faol"),
        default=True
    )


    class Meta:
        verbose_name = _("Footer sozlamasi")
        verbose_name_plural = _("Footer sozlamalari")

    def __str__(self):
        return self.company_name

    def save(self, *args, **kwargs):
        if self.is_active:
            FooterSettings.objects.exclude(pk=self.pk).update(is_active=False)
        super().save(*args, **kwargs)