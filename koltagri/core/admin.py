from django.contrib import admin
from .models import Country

@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    list_display = ("id","name", "abbreviation")  # colunas mostradas
    list_display_links = ("id","name", "abbreviation")  # quais viram links
    search_fields = ("name", "abbreviation")
    ordering = ("name",)