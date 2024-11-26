from django.contrib import admin
from .models import Case, Order, OrderItem

# Register your models here.
# class CaseAdmin(admin.ModelAdmin):
#     list_display = ('id', 'name', 'color', 'material', 'price', 'created_at')
#     search_fields = ('name', 'color', 'material')
#     list_filter = ('color', 'material')
#     ordering = ('created_at',)

# admin.site.register(Case)
# admin.site.register(Order)
# admin.site.register(OrderItem)
# , iPhoneCaseAdmin)

@admin.register(Case)
class CaseAdmin(admin.ModelAdmin):
    list_display = ('name', 'type', 'color', 'material', 'price', 'created_at')
    list_filter = ('type', 'color', 'material', 'price')
    search_fields = ('name', 'type', 'color', 'material')
    ordering = ('type', 'name')
    readonly_fields = ('created_at', 'updated_at')

    fieldsets = (
        ("Basic Information", {
            "fields": ('name', 'type', 'color', 'material', 'price')
        }),
        ("Details", {
            "fields": ('s_description', 'description', 'features'),
        }),
        ("Timestamps", {
            "fields": ('created_at', 'updated_at'),
        }),
    )


class OrderItemInline(admin.TabularInline):
    model = OrderItem
    extra = 1
    readonly_fields = ('total_price',)
    fields = ('case', 'quantity', 'total_price')

    def total_price(self, obj):
        return obj.total_price
    total_price.short_description = 'Total Price (Item)'


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'email', 'phone', 'datetime', 'total_price')
    list_filter = ('datetime',)
    search_fields = ('first_name', 'last_name', 'email', 'phone')
    date_hierarchy = 'datetime'
    readonly_fields = ('datetime', 'total_price')
    inlines = [OrderItemInline]

    def total_price(self, obj):
        return obj.total_price
    total_price.short_description = 'Total Price (Order)'


@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ('order', 'case', 'quantity', 'total_price')
    list_filter = ('case__type',)
    search_fields = ('order__id', 'case__name')
    readonly_fields = ('total_price',)

    def total_price(self, obj):
        return obj.total_price
