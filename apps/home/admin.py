from django.contrib import admin

from apps.home.models import PersonalInfo, Skill


class PersonalInfoAdmin(admin.ModelAdmin):
    list_display = ("first_name", "last_name", "email", "phone", "resume")


class SkillAdmin(admin.ModelAdmin):
    list_display = ("title",)


admin.site.register(PersonalInfo, PersonalInfoAdmin)
admin.site.register(Skill, SkillAdmin)
