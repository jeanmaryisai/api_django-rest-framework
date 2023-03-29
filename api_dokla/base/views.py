from django.shortcuts import render,redirect
from django.http import JsonResponse
from rest_framework.decorators import api_view,permission_classes
from rest_framework.response import Response
from .models import Advocate,Company
from .serializers import AdvocateSerializer,CompanySerializer
from django.db.models import Q
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
# Create your views here.


@api_view(['GET'])
def endpoints(request):
    data=['/advocates','advocates/:username']
    return Response(data)



# @api_view(['GET','POST'])
@permission_classes([IsAuthenticated])
def advocates_list(request):
    if request.method == 'GET':
        query = request.GET.get('query')
        if query == None:
            query =''
        
        advocates=Advocate.objects.filter(Q(bio__icontains=query) | Q(username__icontains=query))
        serializer=AdvocateSerializer(advocates,many=True)
        return Response(serializer.data)
    if request.method == 'POST':
        advocate=Advocate.objects.create(
            username= request.data['username'],
            bio=request.data['bio']
        )
        serializer=AdvocateSerializer(advocate,many=False)
        return Response(serializer.data)



class advocate(APIView):
    def datas(self,username):
        try:
            return Advocate.objects.get(username=username)
        except Advocate.DoesNotExist:
            return Response('The item does not exist')
    
    def get(self, request,username):
        serializer=AdvocateSerializer(self.datas(username),many=False)   
        return Response(serializer.data)
    
    def put(self,request,username):
        advocate=self.datas(username)  
        advocate.username= request.data['username']
        advocate.bio=request.data['bio']
        advocate.save()
        serializer=AdvocateSerializer(advocate,many=False)   
        return Response(serializer.data)
    
    def delete(self,request,username):
        self.datas(username).delete()
        return Response(f'user {username} was deleted')

# @permission_classes([IsAuthenticated])
@api_view(['GET','POST'])
def companies(request):
    if request.method == 'GET':
        
        query = request.GET.get('query')
        if query == None:
            query =''
        
        advocates=Company.objects.filter(Q(bio__icontains=query) | Q(name__icontains=query))
        serializer=CompanySerializer(advocates,many=True)
        return Response(serializer.data)
    
    if request.method == 'POST':
        advocate=Company.objects.create(
            name= request.data['name'],
            bio=request.data['bio']
        )
        serializer=CompanySerializer(advocate,many=False)
        return Response(serializer.data)
    
    return Response('dafa')


# @permission_classes([IsAuthenticated])
@api_view(['GET','PUT','DELETE'])
def company(request,name):
    try:
            datas= Company.objects.get(name=name)
    except Company.DoesNotExist:
            return Response('The item does not exist')

    
    if request.method == 'DELETE':
        datas.delete()
        return Response(f'company {name} was deleted')
    if request.method == 'GET':
        serializer=CompanySerializer(datas,many=False)   
        return Response(serializer.data)
    
    if request.method == 'PUT':
        datas.name= request.data['name']
        datas.bio=request.data['bio']
        datas.save()
    
        serializer=CompanySerializer(datas,many=False)   
        return Response(serializer.data)