from django.contrib import admin
# forma para importar el nuevo modelo(Tex.Im.V) creado a el panel de administrador
from .models import Project

admin.site.register(Project)
