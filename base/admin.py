from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(HomePageNew)
admin.site.register(Vote)
admin.site.register(Choice)
admin.site.register(Question)