from django.contrib import admin

from apidvpt.models import Artist, Album, Songs


# Register your models here.
@admin.register(Artist)
class Artistadmin(admin.ModelAdmin):
    list_display = ['name','email']
    list_per_page = 15
@admin.register(Album)
class Albumadmin(admin.ModelAdmin):
    list_display = ['title','release_year']
    list_per_page = 15
@admin.register(Songs)
class Artistadmin(admin.ModelAdmin):
    list_display = ['track_name','duration']
    list_per_page = 15