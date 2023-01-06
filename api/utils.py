from rest_framework.response import Response
from django.contrib.auth.models import User
from .models import Profile, Note 
from .serializers import ProfileSerializer, NoteSerializer 

def getUsers():
    profiles = Profile.objects.all().order_by('id')
    serializers = ProfileSerializer(profiles, many=True)
    return Response(serializers.data)

def createUser(data):
    user = User.objects.create_user(data['username'], data['email'], data['password'])
    user.save()
    profile = Profile.objects.create(
        user = user,
        name = data['username'],
        email = data['email']
    )
    serializers = ProfileSerializer(profile, many=False)
    return Response(serializers.data)

def getUser(pk):
    profile = Profile.objects.get(id=pk)
    serializers = ProfileSerializer(profile, many=False)
    return Response(serializers.data)

def deleteUser(pk):
    prof = Profile.objects.get(id=pk)
    user = prof.user
    prof.delete()
    user.delete()
    return Response(f'User with id {pk} was deleted')

def getNotes():
    notes = Note.objects.all().order_by('id')
    serializers = NoteSerializer(notes, many=True)
    return Response(serializers.data)

def getUserNotes(pk):
    user = Profile.objects.get(id=pk)
    notes = Note.objects.filter(author=user)
    serializers = NoteSerializer(notes, many=True)
    return Response(serializers.data)

def createNote(data, pk):
    user = Profile.objects.get(id=pk)
    note = Note.objects.create(
        content = data['content'],
        author = user
    )
    serializers = NoteSerializer(note, many=False)
    return Response(serializers.data)

def getNote(pk):
    note = Note.objects.get(id=pk)
    serializers = NoteSerializer(note, many=False)
    return Response(serializers.data)

def deleteNote(pk):
    note = Note.objects.get(id=pk)
    note.delete()
    return Response(f'Note with id {pk} was deleted')