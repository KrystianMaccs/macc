from django.contrib import admin
from apps.home.models import PersonalInfo, Work, Contact, MyContact


class PersonalInfoAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'phone', 'resume')

    
class WorkAdmin(admin.ModelAdmin):
    list_display =('title', )


class ContactAdmin(admin.ModelAdmin):
    list_display = ('subject',)


class MyContactAdmin(admin.ModelAdmin):
    list_display = ('phone_number', 'email', 'address')


admin.site.register(PersonalInfo, PersonalInfoAdmin)
admin.site.register(Contact, ContactAdmin)
admin.site.register(MyContact, MyContactAdmin)
admin.site.register(Work, WorkAdmin)