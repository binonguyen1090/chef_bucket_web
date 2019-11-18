"""
    https://docs.djangoproject.com/en/2.2/howto/static-files/   ---> media image
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('allchefs.urls'))

]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
