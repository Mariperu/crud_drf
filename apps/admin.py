from import_export import resources
from import_export.admin import ImportExportModelAdmin

from django.contrib import admin
from .models import Project


# Register your models here.
#admin.site.register(Project)

#Modelo para import/export
class ProjectResources(resources.ModelResource):
    fields = (
         "title", "description", "technology", "created_at",)
    class Meta:
        model = Project

#Con decoradores
@admin.register(Project)
class ProjectAdmin(ImportExportModelAdmin):
    resource_class = ProjectResources
    list_display = (
        "title", "description",
    )
    search_fields = ("title",)
    list_filter = ("technology",)


