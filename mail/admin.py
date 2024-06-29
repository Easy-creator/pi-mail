from django.contrib import admin
from .models import PassPhrase
# Register your models here.
class YourModelAdmin(admin.ModelAdmin):
    readonly_fields = ('keys',)
    list_display = ('date', 'id',)
    search_fields = ('keys',)

admin.site.register(PassPhrase, YourModelAdmin)