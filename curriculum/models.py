from django.db import models
from django_ckeditor_5.fields import CKEditor5Field



# Create your models here.
class CV(models.Model):
    title = models.CharField(max_length=200, verbose_name="Título")
    content = CKEditor5Field(verbose_name='Contenido', config_name='default')
    image = models.ImageField(verbose_name="Imagen", upload_to="curriculum/")
    texto_boton = models.CharField(max_length=100, verbose_name="Texto del botón", default="Ver más")
    image_position = models.CharField(max_length=50, verbose_name="Posición de la imagen", choices=[("25% 25%", "25% 25%"), ("top center", "Arriba-Centro"), ("center center", "Centro")], default="center center")
    link = models.URLField(verbose_name="Enlace", blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de actualización")
   
     

    class Meta:
        verbose_name = "Entrada"
        verbose_name_plural = "Entradas"
        ordering = ["created"]

    def __str__(self):
        return self.title


