from django.contrib import admin
from movies.models import movies, choices

# Register your models here.
admin.site.register(movies)
admin.site.register(choices)