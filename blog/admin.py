from django.contrib import admin
# con from traemos el modelo desde models y lo
# especificamos al final
from .models import Post

# Register your models here.
# Aqui resgistro el modelo creado en models

admin.site.register(Post)
