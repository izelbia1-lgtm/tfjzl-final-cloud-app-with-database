from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('onlinecourse.urls')),
]

urlpatterns = [
    path('admin/', admin.site.urls),
    path('onlinecourse/', include('onlinecourse.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
