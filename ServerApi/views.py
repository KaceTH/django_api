
from distutils.log import error
from django.shortcuts import render
from django.http import JsonResponse

from django.views.decorators.csrf import csrf_exempt

from ServerApi.models import StudentUser
from ServerApi.serializers import StudentUserSerializer

from rest_framework.parsers import JSONParser

# Create your views here.


@csrf_exempt
def user_list(request):
    if request.method == 'GET':
        query_set = StudentUser.objects.all()
        serializer = StudentUserSerializer(query_set, many= True)
        return JsonResponse(serializer.data, safe=False)
    
    elif request.method == "POST":
        data = JSONParser().parse(request)
        search_user = data['user_id']
        user_data = StudentUser.objects.get(user_id=search_user)
        serializer = StudentUserSerializer(data=data) 

        if data['user_id'] == user_data.user_id:
            return JsonResponse({"Message" : "that user is already exist"}, status=401)
        
        elif serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


@csrf_exempt
def user(request,user_id) :
    try:
        user_data = StudentUser.objects.get(user_id=user_id)
    except: 
        return JsonResponse({"Message" : "data find error"})

    if request.method == 'GET':
        serializer = StudentUserSerializer(user_data)
        return JsonResponse(serializer.data, safe=False)
    
    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = StudentUserSerializer(user_data, data=data)

        if serializer.is_valid():
            return JsonResponse(serializer, status=201)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        user_data.delete()
        return JsonResponse(status=204)


@csrf_exempt
def login(request):
    if request.method == 'POST':
        data = JSONParser().parse(request)
        search_user = data['user_id']
        user_data = StudentUser.objects.get(user_id=search_user)

        if data['user_pw'] == user_data.user_pw:
            return JsonResponse({"Message": "login success"}, status=200)
        else:
            return JsonResponse({"Message" : "login fail"}, status=400)
    
