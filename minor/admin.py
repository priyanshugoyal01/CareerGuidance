from django.contrib import admin

# Register your models here.
from minor.models import Branch, Interest

admin.site.register(Branch)
admin.site.register(Interest)
