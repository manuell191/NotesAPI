from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from .utils import getUsers, createUser, getUser, deleteUser, getNotes, createNote, getUserNotes, getNote, deleteNote, getLogin

'''
POST   /api/login

GET    /api/user
POST   /api/user

GET    /api/user/<pk>
DELETE /api/user/<pk>

GET    /api/user/<pk>/note
POST    /api/user/<pk>/note

GET    /api/note

GET    /api/note/<pk>
DELETE /api/note/<pk>
'''

# Create your views here.

@api_view(['GET'])
def getRoutes(request):
    routes = [
        {
            'Endpoint': '/login/',
            'method': 'POST',
            'body': {
                'username': "",
                'password': ""
            },
            'description': 'Authenticates a user'
        },
        {
            'Endpoint': '/user/',
            'method': 'GET',
            'body': None,
            'description': 'Returns an array of users'
        },
        {
            'Endpoint': '/user/',
            'method': 'POST',
            'body': {
                'username': "",
                'password': "",
                'email': ""
            },
            'description': 'Creates a new user'
        },
        {
            'Endpoint': '/user/id/',
            'method': 'GET',
            'body': None,
            'description': 'Returns a user'
        },
        {
            'Endpoint': '/user/id/',
            'method': 'DELETE',
            'body': None,
            'description': 'Deletes a user'
        },
        {
            'Endpoint': '/user/id/notes',
            'method': 'GET',
            'body': None,
            'description': 'Gets all notes from one user'
        },
        {
            'Endpoint': '/user/id/notes',
            'method': 'POST',
            'body': {
                'content': ""
            },
            'description': 'Creates a new note from user with id'
        },
        {
            'Endpoint': '/note/',
            'method': 'GET',
            'body': None,
            'description': 'Returns an array of notes'
        },
        {
            'Endpoint': '/note/id/',
            'method': 'GET',
            'body': None,
            'description': 'Returns a note'
        },
        {
            'Endpoint': '/note/id/',
            'method': 'DELETE',
            'body': None,
            'description': 'Deletes a note'
        },
    ]
    return Response(routes)

@api_view(['POST'])
def login(request):
    if request.method == 'POST':
        return getLogin(request.data)

@api_view(['GET', 'POST'])
def profiles(request):
    if request.method == 'GET':
        return getUsers()
    elif request.method == 'POST':
        return createUser(request.data)

@api_view(['GET', 'DELETE'])
def profile(request, pk):
    if request.method == 'GET':
        return getUser(pk)
    elif request.method == 'DELETE':
        return deleteUser(pk)

@api_view(['GET'])
def notes(request):
    if request.method == 'GET':
        return getNotes()

@api_view(['GET', 'POST'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def userNotes(request, pk):
    if request.method == 'GET':
        return getUserNotes(request.user, pk)
    elif request.method == 'POST':
        return createNote(request.data, request.user, pk)

@api_view(['GET', 'DELETE'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def note(request, pk):
    if request.method == 'GET':
        return getNote(request.user, pk)
    elif request.method == 'DELETE':
        return deleteNote(request.user, pk)