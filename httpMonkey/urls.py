from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path(
        '',
        include('homepage.urls'),
        name='homepage',
    ),
    path(
        '',
        include('monkeys.urls'),
        name='monkeys',
    ),
    path(
        '',
        include('api.urls'),
        name='api',
    ),
    path(
        'tinymce/',
        include('tinymce.urls'),
        name='tinymce',
    ),
    path(
        'grappelli/',
        include('grappelli.urls'),
        name='grappelli',
    ),
    path(
        'admin/',
        admin.site.urls,
        name='admin',
    ),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

if settings.DEBUG:

    import debug_toolbar

    urlpatterns += [
        path(
            '__debug__/',
            include(
                debug_toolbar.urls,
            ),
        ),
    ]
