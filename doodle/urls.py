"""
URL configuration for doodle project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.urls import views as auth_views
from illustrations import views as illustration_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('illustrations.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('images/<str:image_name>/', illustration_views.serve_image, name='serve_image'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
