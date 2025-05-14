from django.db import models

# Create your models here.
class Proyecto(models.Model):
    title = models.CharField(max_length=200, verbose_name="Título")
    description = models.TextField(verbose_name="Descripción")
    image = models.ImageField(verbose_name="Imagen", upload_to="proyectos")
    link = models.URLField(verbose_name="Enlace", blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de actualización")

    class Meta:
        verbose_name = "Proyecto"
        verbose_name_plural = "Proyectos"
        ordering = ["created"]

    def __str__(self):
        return self.title 
