from django.shortcuts import render

# Create your views here.

from rest_framework.views import APIView

from .models import *
from .serializers import *
from django.http import JsonResponse
from django.contrib.auth.hashers import make_password,check_password
from django.contrib.auth import authenticate, login, logout
from rest_framework.decorators import api_view



class UserActions(APIView):

    def post(self,request):

        try:

            serializer = UserDetailsSerializer(data = request.data)

            if serializer.is_valid():
                hash_password = make_password(serializer.validated_data.get('password'))
                serializer.validated_data['password'] = hash_password
                serializer.save()
                return JsonResponse({'msg':'Registered Successfully'})
                
            return JsonResponse({'msg':serializer.errors})
            
        except Exception as e:
            return JsonResponse({'msg':str(e)})
        


@api_view(["POST"])
def post_login_details(request):

        try:
            print(request.data)

            # hash_password = make_password(request.data.get('password'))
            # print(hash_password)

            user = UserDetails.objects.filter(email = request.data.get('email')).first()
            print(user)

            if user is not None:
                 if check_password(request.data.get('password'),user.password):
                      return JsonResponse({'msg':'logged in successfully'})
                 
                 return JsonResponse({'msg':'Invalid password'})
            
            return JsonResponse({'msg':'Invalid credentials'})
        
        except Exception as e:
             return JsonResponse({'msg':str(e)})
            



        
