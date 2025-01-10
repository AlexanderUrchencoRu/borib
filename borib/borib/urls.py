from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from django.http import Http404
from django.views.static import serve
from main import views

handler403 = 'main.views.tr_handler403'
handler404 = 'main.views.tr_handler404'
handler500 = 'main.views.tr_handler500'

def restricted_media_view(request, path):
    # Проверяем, находится ли запрашиваемый путь в разрешенных папках
    if path.startswith('users_images/') or path.startswith('images_news/'):
        return serve(request, path, document_root=settings.MEDIA_ROOT)
    raise Http404("Доступ запрещен")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name="index"),
    path('users/', include('users.urls', namespace='users')),
    path('messenger/', include('messenger.urls', namespace='messenger')),
    path('media/<path:path>', restricted_media_view, name='restricted_media'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
