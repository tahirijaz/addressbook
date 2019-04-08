# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Contact

# Register your models here.


class ContactAdmin(admin.ModelAdmin):
    search_fields = ['first_name', 'last_name']


admin.site.register(Contact, ContactAdmin)
admin.site.site_header = "Address Book"
