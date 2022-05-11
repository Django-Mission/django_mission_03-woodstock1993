from django.contrib import admin

from support.models import Inquiry, Answer
# Register your models here.

admin.site.register(Answer)


@admin.action(description='답변 완료 안내 발송')
def message_complete(modeladmin, request, queryset):
    for query in queryset:
        if query.is_email:
            print(f'이메일이 있습니다{query.is_email}')
        if query.is_phone:
            print(f'핸드폰이 있습니다.{query.is_phone}')


@admin.register(Inquiry)
class InquiryAdmin(admin.ModelAdmin):
    list_display = ('inquiry_status', 'created_by', 'phone_number','email',)
    search_fields = ['inquiry_status',  'created_by__username', 'user__phone_number', 'user__email']
    list_filter = ('inquiry_status', 'category',)

    actions = [message_complete]

