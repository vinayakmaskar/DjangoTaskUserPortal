

from rest_framework import serializers

from .models import *



class UserDetailsSerializer(models.ModelSerializer):

    username = serializers.charField(max_length=150, unique=True,null = False)
    email = serializers.EmailField(unique=True,null = False)
    password = serializers.charField(max_length=10,null = False)
