from django.contrib import admin

from support.models import Inquiry, Answer, InquiryAdmin
# Register your models here.

admin.site.register([Answer])
admin.site.register(Inquiry, InquiryAdmin)