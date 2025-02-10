from django.contrib import admin
from .models import User, Doctor, News, Date

admin.site.register(User)
admin.site.register(Doctor)
admin.site.register(News)
# admin.site.register(Booking)


@admin.register(Date)
class UserAdmin(admin.ModelAdmin):
    list_display = ("status", "doctor", "date", "time")










