from ckeditor.fields import RichTextField
from django.db import models
from django.utils.safestring import mark_safe
from django_cleanup.signals import cleanup_pre_delete
from sorl.thumbnail import delete, get_thumbnail


class Contact(models.Model):
    link = models.URLField()
    icon = RichTextField()

    @property
    def get_img(self):
        return get_thumbnail(self.upload, '300x300', crop='center', quality=51)

    def img_tmb(self):
        if self.icon:
            return mark_safe(
                f'<img src="{self.get_img.url}">'
            )
        return 'no icons'

    img_tmb.short_description = 'preview'
    img_tmb.allow_tags = True

    def sorl_delete(**kwargs):
        delete(kwargs['file'])

    cleanup_pre_delete.connect(sorl_delete)

    def __str__(self):
        return self.link

    class Meta:
        verbose_name = 'contact'
        verbose_name_plural = 'contacts'
