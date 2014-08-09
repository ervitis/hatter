from django.contrib import admin
from hatter.models import Greeting


class GreetingAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,      {'fields': ['content']}),
        ('Fecha',   {'fields': ['date'], 'classes': ['collapse']}),
    ]

    list_display = ('author', 'content', 'date')

admin.site.register(Greeting, GreetingAdmin)
