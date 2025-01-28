from django.shortcuts import render

# Create your views here.
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import status
from .models import Item
from .serializers import ItemSerializer

class ItemViewSet(ViewSet):
    def list(self, request):
        """List all items."""
        items = Item.objects.all()
        serializer = ItemSerializer(items, many=True)
        return Response(serializer.data)

    def create(self, request):
        """Create a new item."""
        serializer = ItemSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        """Retrieve a single item by ID."""
        try:
            item = Item.objects.get(pk=pk)
        except Item.DoesNotExist:
            return Response({'error': 'Item not found'}, status=status.HTTP_404_NOT_FOUND)
        serializer = ItemSerializer(item)
        return Response(serializer.data)

    def update(self, request, pk=None):
        """Update an existing item."""
        try:
            item = Item.objects.get(pk=pk)
        except Item.DoesNotExist:
            return Response({'error': 'Item not found'}, status=status.HTTP_404_NOT_FOUND)
        serializer = ItemSerializer(item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        """Delete an item."""
        try:
            item = Item.objects.get(pk=pk)
            item.delete()
            return Response({'message': 'Item deleted successfully'}, status=status.HTTP_204_NO_CONTENT)
        except Item.DoesNotExist:
            return Response({'error': 'Item not found'}, status=status.HTTP_404_NOT_FOUND)
