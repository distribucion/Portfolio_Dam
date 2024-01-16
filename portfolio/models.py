from django.db import models
# forma para importar datos
from django.db.models.fields import CharField, URLField
# forma para importar imagenes
from django.db.models.fields.files import ImageField


# Guardar los datos de mi portafolio
# Saving my porrfolio data


class Project(models.Model):
    title = CharField(max_length=100)
    description = CharField(max_length=800)
    image = ImageField(upload_to="portfolio/images/")
    url = URLField(blank=True)
    url2 = URLField(blank=True)
    video = models.FileField(
        upload_to='portfolio/videos/', blank=True, null=True)
