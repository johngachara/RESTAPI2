from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response

from apidvpt.models import Artist
from apidvpt.serializers import Artistserializer,AtristAlbumserializer


# Create your views here.
@api_view(['GET'])
def get_artists(request):
    if request.method == 'GET':
        artists = Artist.objects.all()
        serializer = Artistserializer(many=True,instance=artists)
        return Response({"artists":serializer.data})


@api_view(['GET'])
def get_artist(request, id):
    try:
        artist = Artist.objects.get(pk=id)
        serializer = Artistserializer(instance=artist)
        return Response({"Artist":serializer.data})
    except:
        return Response({"Error":"Artist with given id not found"})


@api_view(['POST'])
def create_artist(request):
    if request.method == 'POST':
        serializer = Artistserializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response({"Message":"Added successfully","data":serializer.data})

@api_view(['PUT','PATCH'])
def update_artist(request,id):
    try:
        artist = Artist.objects.get(pk=id)
        serializer = Artistserializer(instance=artist,data=request.data,partial=True)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response({"message":"updated Successfully","Updated artist":serializer.data})
    except:
        return Response({"Error":"Artist with given id not found"})


@api_view(['DELETE'])
def delete_artist(request,id):
    try:
        artist = Artist.objects.get(pk=id)
        if artist:
            artist.delete()
            return Response({"message":'deleted successfully'})
    except:
        return Response({"Error":"Artist not found"})



@api_view(['GET'])
def get_album_for_artist(request,id):
    try:
        artist = Artist.objects.get(pk=id)
        serializer = AtristAlbumserializer(instance=artist)
        return Response({"Artist":serializer.data})
    except:
        return Response({"Error":"Artist not Found"})

def home(request):
    return render(request,'home.html')