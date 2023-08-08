from django.shortcuts import render

# Create your views here.

from rest_framework.views import APIView

from .models import *
from .serializers import *
from django.http import JsonResponse
from django.contrib.auth.hashers import make_password 


class UserActions(APIView):

    def post(self,request):

        try:

            hash_password = make_password(request.data.get('password'))
            request.data['password'] = hash_password
            serializer = UserDetailsSerializer(data = request.data)
            print(request.data)

            if serializer.is_valid():
                serializer.save()
                return JsonResponse({'msg':'Registered Successfully'})
                
            return JsonResponse({'msg':serializer.errors})
            
        except Exception as e:
            return JsonResponse({'msg':str(e)})

        
