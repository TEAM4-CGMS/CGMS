from django.contrib import admin
# Register your models here.
from .models import Contact

from import_export.admin import ImportExportModelAdmin
# Register your models here.
@admin.register(Contact)

class myclass(ImportExportModelAdmin):
    pass