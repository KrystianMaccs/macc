from rest_framework import serializers
from apps.home.models import PersonalInfo, Work, Contact, MyContact


class PersonalInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = PersonalInfo
        fields = "__all__"


class WorkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Work
        fields = "__all__"

class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = "__all__"

class MyContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyContact
        fields = "__all__"