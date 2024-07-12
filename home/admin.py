from django.contrib import admin
from .models import Departments,Doctors,Booking
# Register your models here.
admin.site.register(Departments)
admin.site.register(Doctors)
class Bookingadmin(admin.ModelAdmin):
    list_display = ( ('id', 'p_name', 'p_email', 'p_phone', 'doc_name','booking_date', 'booked_on' ))
admin.site.register(Booking,Bookingadmin)