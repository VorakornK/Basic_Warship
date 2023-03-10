from django.contrib import admin
from HttpMethods.models import Board, Player, Ship, Update

# Register your models here.
admin.site.register(Board)
admin.site.register(Player)
admin.site.register(Ship)
admin.site.register(Update)