from django.contrib import admin
from .models import Ticket
from .models import Product
from import_export.admin import ImportExportModelAdmin

@admin.register(Ticket)
@admin.register(Product)

class myclass(ImportExportModelAdmin):
    pass