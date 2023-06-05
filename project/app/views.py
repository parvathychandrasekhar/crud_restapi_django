from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import serializers
from rest_framework import status
from django.shortcuts import get_object_or_404

from .models import Item
from .serializers import ItemSerializer

class ApiOverview(APIView):
    def get(self, request):
        api_urls = {
            'all_items': '/',
            'Search by Category': '/?category=category_name',
            'Search by Subcategory': '/?subcategory=category_name',
            'Add': '/create',
            'Update': '/update/pk',
            'Delete': '/item/pk/delete'
        }
        return Response(api_urls)

class AddItems(APIView):
    def post(self, request):
        item = ItemSerializer(data=request.data)

        # validating for already existing data
        if Item.objects.filter(**request.data).exists():
            raise serializers.ValidationError('This data already exists')

        if item.is_valid():
            item.save()
            return Response(item.data, status=status.HTTP_201_CREATED)
        else:
            return Response(item.errors, status=status.HTTP_400_BAD_REQUEST)


class ViewItems(APIView):
    def get(self, request):
        # checking for the parameters from the URL
        if request.query_params:
            items = Item.objects.filter(**request.query_params.dict())
        else:
            items = Item.objects.all()

        # if there is something in items else raise error
        if items:
            serializer = ItemSerializer(items, many=True)
            return Response(serializer.data)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)

class UpdateItems(APIView):
    def put(self, request, pk):
        item = Item.objects.get(pk=pk)
        data = ItemSerializer(instance=item, data=request.data)

        if data.is_valid():
            data.save()
            return Response(data.data)
        else:
            return Response(data.errors, status=status.HTTP_400_BAD_REQUEST)

class DeleteItems(APIView):
    def delete(self, request, pk):
        item = get_object_or_404(Item, pk=pk)
        item.delete()
        return Response(status=status.HTTP_202_ACCEPTED)