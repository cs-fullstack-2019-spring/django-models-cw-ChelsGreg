from django.contrib import admin

# Register your models here.

from .models import Dog
from .models import Account

# REGISTER CLASSES ONTO SITE
admin.site.register(Dog)
admin.site.register(Account)