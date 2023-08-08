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
                # print(serializer.data)  // cant write this before serializer.save() instead serializer.validated_data
                hash_password = make_password(serializer.validated_data.get('password'))
                serializer.validated_data['password'] = hash_password
                serializer.save()
                return JsonResponse({'msg':'Registered Successfully','data' : serializer.data},status=201)
                
            return JsonResponse({'msg':serializer.errors}, status = 400)
            
        except Exception as e:
            return JsonResponse({'msg':str(e)}, status = 500)
        


@api_view(["POST"])
def post_login_details(request):

        try:

            if request.data.get("email") is None or  not request.data.get("email").strip():
                 return JsonResponse({'msg':'email required'})
            
            if request.data.get("password") is None or not request.data.get("password").strip():
                 return JsonResponse({'msg':'Password required'})
            

            serializer = UserDetailsSerializer(data =request.data, partial = True)

            if serializer.is_valid():
                    

                print(request.data)
                user = UserDetails.objects.filter(email = request.data.get('email')).first()
                print(user)

                if user is not None:
                    if check_password(request.data.get('password'),user.password):
                        return JsonResponse({'msg':'logged in successfully'})
                    
                    return JsonResponse({'msg':'Invalid password'})
                
                return JsonResponse({'msg':'Invalid email'})
            
            return JsonResponse({'msg':serializer.errors})
        
        except Exception as e:
                # print("hell")
                return JsonResponse({'msg':str(e)})
                



        
