from django.db import models
from django.utils.timezone import now
from django.contrib.auth.models import User
from django_ckeditor_5.fields import CKEditor5Field

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name="Nombre")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de actualización")
   
     

    class Meta:
        verbose_name = "categoría"
        verbose_name_plural = "categorías"
        ordering = ["created"]

    def __str__(self):
        return self.name
    
class Post(models.Model):
    title = models.CharField(max_length=200, verbose_name="Título")
    content = CKEditor5Field(verbose_name='Contenido', config_name='default')
    order = models.SmallIntegerField(verbose_name="Orden", default=0, null=True, blank=True)
    published = models.DateTimeField(verbose_name="Fecha de publicación", default=now)
    image = models.ImageField(verbose_name="Imagen", upload_to="blog", null=True, blank=True)
    author = models.ForeignKey(User, verbose_name="Autor", on_delete=models.CASCADE)
    categories = models.ManyToManyField(Category, verbose_name="Categorías", related_name="get_posts")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de actualización")

    class Meta:
        verbose_name = "entrada"
        verbose_name_plural = "entradas"
        ordering = ["-created", "order"]

    def __str__(self):
        return self.title