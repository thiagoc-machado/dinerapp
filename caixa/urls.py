from django.contrib import admin
from django.urls import include, path
from django.conf.urls.static import static
from django.conf import settings
from . import views



urlpatterns = [
    path('', views.dashboard, name="dashboard"),


]# + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
# + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)