"""exxen URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from xml.dom.minidom import Document
from django.contrib import admin
from django.urls import path, include
# medıa için dosyalarımın görüntelnmesi için gereken importlar
# static de yazdıgımız yer static css javsascript ve media larda kullanılır
from django.conf.urls.static import static
from django.conf import settings
# alt tarafta url lerimizi belirliyoruz sayfa url lerini

#  http://127.0.0.1:8000/
urlpatterns = [
    path('admin/', admin.site.urls),
    #   movies klasorunun içindeki urls.py ı ana urls.py a baglıyoruz
    path('', include('movies.urls')),
    path('user/', include("user.urls"))
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
# bu resimlerin gosterilmesi için gerekli olan kod