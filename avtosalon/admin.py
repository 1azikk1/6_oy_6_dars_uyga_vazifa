from django.contrib import admin
from .models import Brand, Car
from django.utils.safestring import mark_safe

admin.site.register(Brand)


class AdminCar(admin.ModelAdmin):
    list_display = ('id', 'name', 'color', 'year', 'price', 'horsepower', 'added', 'brand', 'views', 'get_photo')
    list_display_links = ('name', 'id')
    list_editable = ('color', 'year', 'price', 'horsepower', 'brand')
    list_filter = ('brand', 'is_available')
    search_fields = ('name', 'year')
    list_per_page = 10
    actions_on_top = False
    actions_on_bottom = True
    readonly_fields = ('views',)

    def get_photo(self, car):
        if car.photo:
            return mark_safe(f'<img src="{car.photo.url}" width="200px">')
        return 'Rasm topilmadi!'

    get_photo.short_description = 'Rasmi'


admin.site.register(Car, AdminCar)
