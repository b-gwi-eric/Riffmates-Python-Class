from django.contrib import admin
from band.models import Musician 
# Register your models here.

@admin.register(Musician)
class MusicianAdmin(admin.ModelAdmin):
    pass
