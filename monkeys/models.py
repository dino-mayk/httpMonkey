from django.db import models
from django.utils.safestring import mark_safe
from django_cleanup.signals import cleanup_pre_delete
from sorl.thumbnail import delete, get_thumbnail
from tinymce.models import HTMLField


class Monkey(models.Model):
    code = models.SmallIntegerField()
    title = models.CharField(
        unique=True,
        max_length=25,
    )
    image = models.ImageField(
        upload_to='images/monkeys/%Y/%m',
        verbose_name="image",
        help_text='load image'
    )
    description = HTMLField()

    @property
    def get_img(self):
        return get_thumbnail(self.upload, '300x300', crop='center', quality=51)

    def img_tmb(self):
        if self.image:
            return mark_safe(
                f'<img src="{self.get_img.url}">'
            )
        return 'no images'

    img_tmb.short_description = 'preview'
    img_tmb.allow_tags = True

    def sorl_delete(**kwargs):
        delete(kwargs['file'])

    cleanup_pre_delete.connect(sorl_delete)

    def __str__(self):
        return self.image.url

    class Meta:
        verbose_name = 'monkey'
        verbose_name_plural = 'monkeys'
