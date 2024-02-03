"""
URL configuration for django_portfolio project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
# from django.contrib import admin
# from django.urls import path

# urlpatterns = [
#     path('admin/', admin.site.urls),
# ]


# aqui comenzo#####

# from django.contrib import admin
# from django.urls import path, include

# from django.conf.urls.static import static
# from django.conf import settings
# from portfolio import views


# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('', views.home, name='home'),
#     path('blog/', include('blog.urls'))


# ]

# urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


from django.contrib import admin
from django.urls import path, include
from portfolio import views

# Definición de urlpatterns para tu proyecto Django
urlpatterns = [
    path('admin/', admin.site.urls),  # Ruta para el administrador de Django
    # Ruta para la vista 'home' de la app 'portfolio'
    path('', views.home, name='home'),
    path('blog/', include('blog.urls')),  # Incluye las URLs de la app 'blog'
]

# No es necesario añadir rutas para servir archivos estáticos y multimedia en producción
# ya que se servirán directamente desde Azure Blob Storage según configuración en settings.py
