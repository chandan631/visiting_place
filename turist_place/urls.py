from django.contrib import admin
from django.urls import path
from place import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.display),
    # path('add_state', views.add_state),
    path('add_district', views.add_district),
    path('add_page', views.add_page),
    path('admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


