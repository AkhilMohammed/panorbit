from rest_framework import serializers
from zeroapp.models import signup

class signupserializer(serializers.ModelSerializer):
    class META:
        model=signup
        fields=['firstname','lastname','gender','email','mobile']

