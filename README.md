# NotesAPI
API for fullstack Notes Project



## Overview

This API is for a fullstack project that I am creating with
Django in the backend and React in the front end. This is a
RESTful API with the following methods and endpoints:

```
GET    /api/user
POST   /api/user

GET    /api/user/<pk>
DELETE /api/user/<pk>

GET    /api/user/<pk>/note
POST    /api/user/<pk>/note

GET    /api/note

GET    /api/note/<pk>
DELETE /api/note/<pk>
```



## User Methods

### /api/user

#### GET Method

`GET /api/user` will return a list of all users in the following 
json format:
```
[{
  "id": "1",
  "user": "{User object}",
  "name": "user1",
  "email": "use1r@email.com"
}]
```

The `{User object}` is a foreign key to the `User` table which 
is automatically generated by the Django Framework. In json, 
it will appear as the id from the `User` object. The reason 
that the database was built in this way is to avoid tinkering
with the built in `User` class to avoid any security problems.

#### POST Method

`POST /api/user` will take in a json request and create a new
user. The request should be in the following format:
```
{
  "username": "user2",
  "password": "password123",
  "email": "user2@email.com"
}
```

The call will return a respnose which will also include only
this user in the same format as `GET /api/user`.


### /api/user/<id>

#### GET Method

`GET /api/user/<id>` takes a number replacing `<id>` and returns
a user with id matching that number. Keep in mind that this will
return data from the Profile table rather than from the User table.
The response will be returned in the following format:
```
{
  "id": "2",
  "user": "{User object}",
  "name": "user2",
  "email": "user2@email.com"
}
```

This specific response would come from `GET /api/user/2` since
the id is equal to 2.

#### DELETE Method

`DELETE /api/user/<id>` takes a number replacing `<id>` and
deletes a user with id matching that number. This will delete
the user from both the User and Profile tables. This method
will only return: `User with id 2 was deleted`. This specific
response would come from `DELETE /api/user/2` since the id is
equal to 2.



## Note Methods

### /api/note

#### GET Method

`GET /api/note` will return a list of all notes in the
following format:
```
[{
  "id": "1",
  "content": "This is a note",
  "author": "{Profile object}"
}]
```

The `{Profile object}` is a foreign key to the `Profile` table. 
In json, it will appear as the id from the `Profile` object.


### /api/note/<id>

#### GET Method

`GET /api/note/<id>` takes a number replacing `<id>` and returns
a note with id matching that number. The response will be returned
in the following format:
```
{
  "id": "2",
  "content": "This is a new note",
  "author": "{Profile object}"
}
```

This specific response would come from `GET /api/note/2` since
the id is equal to 2.

#### DELETE Method

`DELETE /api/note/<id>` takes a number replacing `<id>` and
deletes a note with id matching that number. This will delete
the note from the Note table. This method will only return:
`Note with id 2 was deleted`. This specific response would 
come from `DELETE /api/user/2` since the id is equal to 2.



## Other Methods

### /api/user/<id>/note

#### GET Method

`GET /api/user/<id>/note` takes a number replacing `<id>`
and returns all notes from a user with id matching that
number. The response will be returned in the following format:
```
[{
  "id": "2",
  "content": "This is a new note",
  "author": "{Profile object}"
}]
```

This specific response could come from `GET /api/user/1/note`
as long as the `{Profile object}` in this instance is a profile
with the id of 1.

#### POST Method

`POST /api/user/<id>/note` takes a number replacing
`<id>` and will create a note for the user with id matching
that number. The reason the API is built like this is to make
the response smaller by taking out the author section in the
request's body. The request would be made in the following format:
```
{
  "content": "This is a new note"
}
```

This specific response could come from `POST /api/user/1/note`
if you wanted to make the author to this note be a user with an
id of 1.


### /api

#### GET Method

`GET /api` will return the routes you can use with a small
description and guide on how to send the json request.


