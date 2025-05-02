from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from loyer import views as loyer_views

app_name = 'authenticate'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('authenticate.urls')),
    path('loyer/', include('loyer.urls')),
    path('immeuble/<int:immeuble_id>/', loyer_views.immeuble_detail, name='immeuble_detail'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
