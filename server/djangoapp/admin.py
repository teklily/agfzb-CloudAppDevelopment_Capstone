from django.contrib import admin
from .models import CarMake, CarModel
# from .models import related models


# Register your models here.

# CarModelInline class
class CarModelInline(admin.StackedInline):
    model=CarModel
    extra=1
# CarModelAdmin class
class CarModelAdmin(admin.ModelAdmin):
    list_display = ['make', 'name', 'id', 'type', 'year']
    list_filter = ['type', 'make', 'id', 'year',]
    search_fields = ['make', 'name']
    #inlines = [CarModelInline]
# CarMakeAdmin class with CarModelInline
class CarMakeAdmin(admin.ModelAdmin):
    list_display=("name", "description")
    inlines=[CarModelInline]
# Register models here
admin.site.register(CarMake, CarMakeAdmin)
admin.site.register(CarModel, CarModelAdmin)