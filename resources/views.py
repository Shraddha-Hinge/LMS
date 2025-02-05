# resources/views.py
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Folder, Resource
from .serializers import FolderSerializer, ResourceSerializer

class FolderListView(APIView):
    def get(self, request):
        folders = Folder.objects.all()
        serializer = FolderSerializer(folders, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = FolderSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class FolderDetailView(APIView):
    def get_object(self, pk):
        try:
            return Folder.objects.get(pk=pk)
        except Folder.DoesNotExist:
            return None

    def get(self, request, pk):
        folder = self.get_object(pk)
        if folder is None:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = FolderSerializer(folder)
        return Response(serializer.data)

    def put(self, request, pk):
        folder = self.get_object(pk)
        if folder is None:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = FolderSerializer(folder, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        folder = self.get_object(pk)
        if folder is None:
            return Response(status=status.HTTP_404_NOT_FOUND)
        folder.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class ResourceListView(APIView):
    def get(self, request):
        resources = Resource.objects.all()
        serializer = ResourceSerializer(resources, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ResourceSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ResourceDetailView(APIView):
    def get_object(self, pk):
        try:
            return Resource.objects.get(pk=pk)
        except Resource.DoesNotExist:
            return None

    def get(self, request, pk):
        resource = self.get_object(pk)
        if resource is None:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = ResourceSerializer(resource)
        return Response(serializer.data)

    def put(self, request, pk):
        resource = self.get_object(pk)
        if resource is None:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = ResourceSerializer(resource, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        resource = self.get_object(pk)
        if resource is None:
            return Response(status=status.HTTP_404_NOT_FOUND)
        resource.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)










"""from rest_framework import status, viewsets
from rest_framework.response import Response
from .models import Folder, Resource
from .serializers import FolderSerializer, ResourceSerializer

class FolderViewSet(viewsets.ModelViewSet):
    queryset = Folder.objects.all()
    serializer_class = FolderSerializer


class ResourceViewSet(viewsets.ModelViewSet):
    queryset = Resource.objects.all()
    serializer_class = ResourceSerializer

    def create(self, request, *args, **kwargs):
        folder = request.data.get('folder')
        folder_instance = Folder.objects.get(id=folder)  # Ensure the folder exists
        resource = request.data.copy()
        resource['folder'] = folder_instance.id
        return super().create(request, *args, **kwargs)"""
    


"""from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from .models import Folder, Resource
from django.urls import reverse_lazy

class FolderListView(ListView):
    model = Folder
    template_name = 'resources/folder_list.html'
    context_object_name = 'folders'

class FolderCreateView(CreateView):
    model = Folder
    template_name = 'resources/folder_form.html'
    fields = ['name']

class FolderDetailView(DetailView):
    model = Folder
    template_name = 'resources/folder_detail.html'
    context_object_name = 'folder'

class FolderUpdateView(UpdateView):
    model = Folder
    template_name = 'resources/folder_form.html'
    fields = ['name']

class FolderDeleteView(DeleteView):
    model = Folder
    template_name = 'resources/folder_confirm_delete.html'
    success_url = reverse_lazy('folder_list')

class ResourceListView(ListView):
    model = Resource
    template_name = 'resources/resource_list.html'
    context_object_name = 'resources'

class ResourceCreateView(CreateView):
    model = Resource
    template_name = 'resources/resource_form.html'
    fields = ['name', 'folder', 'file']

class ResourceDetailView(DetailView):
    model = Resource
    template_name = 'resources/resource_detail.html'
    context_object_name = 'resource'

class ResourceUpdateView(UpdateView):
    model = Resource
    template_name = 'resources/resource_form.html'
    fields = ['name', 'folder', 'file']

class ResourceDeleteView(DeleteView):
    model = Resource
    template_name = 'resources/resource_confirm_delete.html'
    success_url = reverse_lazy('resource_list')
"""