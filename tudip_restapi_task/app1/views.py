from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.status import HTTP_201_CREATED
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .serializers import Candidate_Serializer
from .models import Candidate
from rest_framework.filters import SearchFilter,OrderingFilter
# Create your views here.
class User_List(ListCreateAPIView):
    queryset = Candidate.objects.all()
    serializer_class = Candidate_Serializer
    filter_backends = [SearchFilter,OrderingFilter]
    search_fields = ['id','name','phone','address']
    ordering_fields = ['id', 'name', 'phone', 'address']

class User_Update(RetrieveUpdateDestroyAPIView):
    queryset = Candidate.objects.all()
    serializer_class = Candidate_Serializer


    # def get(self,request,pk=None,format=None):
    #     id = pk
    #     if id is not None:
    #         user = Candidate.objects.get(id=id)
    #         serializer = Candidate_Serializer(user)
    #         return Response(serializer.data)
    #     paginator = PageNumberPagination()
    #     user = Candidate.objects.all()
    #     paginator.page_size = 5
    #     result_page = paginator.paginate_queryset(user, request)
    #     serializer = Candidate_Serializer(result_page, many=True)
    #     return paginator.get_paginated_response(serializer.data)
    #
    #
    # def post(self,request,format=None):
    #     serializer = Candidate_Serializer(data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         res = {'msg':'Data has been Created Successfully'}
    #         return Response(res,status=HTTP_201_CREATED)
    #     return Response(serializer.errors)
    #
    # def put(self, request,pk,format=None):
    #     user = Candidate.objects.get(pk=id)
    #     serializer = Candidate_Serializer(user,data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response({'msg':'Data Updated'})
    #     return Response(serializer.errors)
    #
    # def patch(self, request, pk, format=None):
    #     id = request.data.get('id')
    #     user = Candidate.objects.get(pk=id)
    #     serializer = Candidate_Serializer(user,data=request.data,partial=True)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response({'msg':'Data Updated'})
    #     return Response(serializer.errors)
    #
    # def delete(self, request, pk, format=None):
    #     id = pk
    #     user = Candidate.objects.get(pk=id)
    #     user.delete()
    #     return Response({'msg':'Data Deleted'})