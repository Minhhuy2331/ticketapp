from django.contrib import admin
from django.db.models import Count
from django.template.response import TemplateResponse
from django.urls import path
from django.utils.safestring import mark_safe

from .models import *


class TicketAdmin(admin.ModelAdmin):
    search_fields = ['name']
    list_filter = ['booking_date']
    list_display = ['name', 'booking_date']


class CarAdmin(admin.ModelAdmin):
    search_fields = ['name']
    list_filter = ['number_of_seats', 'range_of_vehicle']
    list_display = ['name', 'range_of_vehicle', 'number_of_seats']


class BusroutesAdmin(admin.ModelAdmin):
    search_fields = ['name']
    list_filter = ['point_of_departure', 'destination']
    list_display = ['name', 'point_of_departure', 'destination', 'pricelist']

    def get_urls(self):
        return [
                   path('ticket-stats/', self.stats_view)
               ] + super().get_urls()

    def stats_view(self, request):
        c = Busroutes.objects.filter(active=True).count()
        stats = Busroutes.objects.annotate(Busroutes_count=Count('ticket_details'))

        return TemplateResponse(request,
                                'admin/ticket-stats.html', {
                                    'count': c,
                                    'stats': stats
                                })


class Ticket_detailsAdmin(admin.ModelAdmin):
    search_fields = ['Ticket']
    list_filter = ['seats', 'Busroutes', 'car', 'user']
    list_display = ['id', 'seats', 'Busroutes', 'car', 'user']


admin.site.register(User)
admin.site.register(Ticket, TicketAdmin)
admin.site.register(Busroutes, BusroutesAdmin)
admin.site.register(Ticket_details, Ticket_detailsAdmin)
admin.site.register(Range_of_vehicle)
admin.site.register(Car, CarAdmin)
admin.site.register(Bus)
