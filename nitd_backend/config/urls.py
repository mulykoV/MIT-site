from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('department.urls')), # <--- Наш новий шлях API
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) # Дозвіл на віддачу картинок