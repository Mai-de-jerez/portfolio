from django.contrib import admin
from .models import CV

# Register your models here.
class CVAdmin(admin.ModelAdmin):
    readonly_fields = ("created", "updated")
    ordering = ("-created",)
    list_display = ("title", "created", "updated")
    list_filter = ("created", "updated")
    search_fields = ("title",)

admin.site.register(CV, CVAdmin)