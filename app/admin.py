from django.contrib import admin
from app.models import Point


class PointAdmin(admin.ModelAdmin):
    pass
admin.site.register(Point, PointAdmin)
