from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from .models import Profile, Note 
from .serializers import ProfileSerializer, NoteSerializer 

def getLogin(data):
    username = data['username']
    password = data['password']
    user = User.objects.get(username=username)
    success = user.check_password(password)
    if success:
        token = Token.objects.get_or_create(user=user)
        return Response({"token": token[0].key})
    return Response('Incorrect username or password')

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

def getUserNotes(user, pk):
    prof = Profile.objects.get(id=pk)
    if user != prof:
        return Response({"detail": "You do not have permission to perform this action."}, status=status.HTTP_403_FORBIDDEN)
    notes = Note.objects.filter(author=prof)
    serializers = NoteSerializer(notes, many=True)
    return Response(serializers.data)

def createNote(data, user, pk):
    prof = Profile.objects.get(id=pk)
    if user != prof:
        return Response({"detail": "You do not have permission to perform this action."}, status=status.HTTP_403_FORBIDDEN)
    note = Note.objects.create(
        content = data['content'],
        author = prof
    )
    serializers = NoteSerializer(note, many=False)
    return Response(serializers.data)

def getNote(user, pk):
    note = Note.objects.get(id=pk)
    if user != note.author.user:
        return Response({"detail": "You do not have permission to perform this action."}, status=status.HTTP_403_FORBIDDEN)
    serializers = NoteSerializer(note, many=False)
    return Response(serializers.data)

def deleteNote(user, pk):
    note = Note.objects.get(id=pk)
    if user != note.author.user:
        return Response({"detail": "You do not have permission to perform this action."}, status=status.HTTP_403_FORBIDDEN)
    note.delete()
    return Response(f'Note with id {pk} was deleted')