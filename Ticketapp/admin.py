from django.contrib import admin

from .models import *

admin.site.register(User)
admin.site.register(Ticket)
admin.site.register(Buses)
admin.site.register(Ticket_details)
admin.site.register(Range_of_vehicle)
admin.site.register(Car)

