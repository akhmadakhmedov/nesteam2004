from django.contrib import admin
from .models import *


admin.site.register(Game)
admin.site.register(Genre)



class GameInline(admin.StackedInline):
    model = Game
    extra = 1

@admin.register(Studio)
class StudioAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'workers_count', 'games_count']
    inlines = [GameInline]


