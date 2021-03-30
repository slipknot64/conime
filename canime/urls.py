from django.urls import path
from . import views
from django.urls import include
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('conime', views.conime, name='conime'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)