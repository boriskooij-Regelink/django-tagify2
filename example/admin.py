from django.contrib import admin

from example.forms import PeopleAdminForm
from example.models import People


@admin.register(People)
class PeopleAdmin(admin.ModelAdmin):
    form = PeopleAdminForm
    list_display = ["languages", "test"]
    list_filter = ["languages", "test"]
    search_fields = ["languages", "test"]

    def save_model(self, request, obj, form, change):
        print(obj.languages)

        super().save_model(request, obj, form, change)
