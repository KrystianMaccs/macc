from rest_framework import serializers

from apps.home.models import PersonalInfo, Skill


class PersonalInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = PersonalInfo
        fields = ["first_name", "last_name", "phone", "email", "address", "resume"]


class SkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skill
        fields = "__all__"
