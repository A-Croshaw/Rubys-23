from django.contrib import admin
from .models import Order, OrderLineTotal


class OrderLineTotalAdminInline(admin.TabularInline):
    model = OrderLineTotal
    readonly_fields = ('itemline_total',)


class OrderAdmin(admin.ModelAdmin):
    inlines = (OrderLineTotalAdminInline,)

    readonly_fields = ('order_number', 'date',
                       'delivery_cost', 'order_total',
                       'overal_total', 'original_cart',
                       'stripe_pid')

    fields = ('order_number', 'profile', 'date', 'full_name',
              'email', 'phone_number', 'country',
              'postcode', 'town_or_city', 'street_address1',
              'street_address2', 'county', 'delivery_cost',
              'order_total', 'overal_total', 'original_cart',
              'stripe_pid')

    list_display = ('order_number', 'date', 'full_name',
                    'order_total', 'delivery_cost',
                    'overal_total',)

    ordering = ('-date',)

admin.site.register(Order, OrderAdmin)