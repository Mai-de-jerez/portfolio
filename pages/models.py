from django.db import models
from django_ckeditor_5.fields import CKEditor5Field

# Create your models here.
class Page(models.Model):
    title = models.CharField(verbose_name="Título", max_length=200)
    content = CKEditor5Field(verbose_name='Contenido', config_name='default')
    order = models.SmallIntegerField(verbose_name="Orden", default=0)
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de actualización")
   
     

    class Meta:
        verbose_name = "página"
        verbose_name_plural = "páginas"
        ordering = ["order", "title"]

    def __str__(self):
        return self.title
