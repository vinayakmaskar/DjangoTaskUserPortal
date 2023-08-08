
import re
from rest_framework import serializers

from .models import *

class UserDetailsSerializer(serializers.ModelSerializer):

    # username = serializers.CharField()
    email = serializers.CharField()
    phonenumber = serializers.CharField()
    password = serializers.CharField()

    class Meta:
        model = UserDetails
        fields = "__all__"


    # def validate_email(self,value):

    #     if not re.match(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.(com|in)$', value):
    #         raise serializers.ValidationError("Invalid email format. Only .com and .in domains are allowed.")


    #     if UserDetails.objects.filter(email = value).exists():
    #         raise serializers.ValidationError("email already exists")
        

    #     return value
    

    # def validate_phonenumber(self,value):

    #     if not re.match(r'^\d{10}$', value):
    #         raise serializers.ValidationError("Invalid phone number format. Please enter a 10-digit number.")

    #     if UserDetails.objects.filter(phonenumber=value).exists():
    #         raise serializers.ValidationError("Phone number already exists")
        
    #     return value
    
    # def validate_username(self,value):
    #     if UserDetails.objects.filter(username = value).exists():
    #         raise serializers.ValidationError("Username already exists")
        
    #     return value
    

    def validate(self,data):
        email = data.get('email')
        phonenumber = data.get('phonenumber')
        password = data.get('password')


        if not re.match(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.(com|in)$', email):
            raise serializers.ValidationError("Invalid email format. Only .com and .in domains are allowed.")

        if not re.match(r'^\d{10}$', phonenumber):
            raise serializers.ValidationError("Invalid phone number format. Please enter a 10-digit number.")
        
        if not re.match(r'^(?=.*[A-Z])(?=.*[0-9])(?=.*[!@#$%^&*(),.?":{}|<>]).{8,}$',password):
            raise serializers.ValidationError("It must contain at least one uppercase letter, one lowercase letter, one digit, and one special character and lenght should be 8")


        return data


    

