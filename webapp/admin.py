from django.contrib import admin
from .models import Case

# Register your models here.
# class CaseAdmin(admin.ModelAdmin):
#     list_display = ('id', 'name', 'color', 'material', 'price', 'created_at')
#     search_fields = ('name', 'color', 'material')
#     list_filter = ('color', 'material')
#     ordering = ('created_at',)

admin.site.register(Case)
# , iPhoneCaseAdmin)
