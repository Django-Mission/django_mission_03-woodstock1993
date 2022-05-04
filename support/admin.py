from django.contrib import admin

from support.models import Inquiry, Answer, UserAdmin

# Register your models here.

admin.site.register([Inquiry, Answer, UserAdmin])