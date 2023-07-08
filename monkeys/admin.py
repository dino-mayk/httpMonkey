from django.contrib import admin

from monkeys.models import Monkey


@admin.register(Monkey)
class MonkeyAdmin(admin.ModelAdmin):
    list_display = [
        'code',
    ]
