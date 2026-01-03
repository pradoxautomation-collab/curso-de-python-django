from django.contrib import admin
from django.urls import path, include # Adicionamos o 'include' aqui
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    # Esta linha abaixo conecta o seu site à lógica dos cursos
    path('', include('courses.urls')), 
]

# Adiciona o caminho das imagens apenas em modo de desenvolvimento
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)