import json
from django.http import HttpResponse
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from django.views.decorators.csrf import csrf_exempt
from raterprojectapi.models import Players
from rest_framework.viewsets import ViewSet
from raterprojectapi.serializers import UsersSerializer
from rest_framework.response import Response
from django.http import HttpResponseServerError

class PlayersViewSet(ViewSet):
    
    def retrieve(self, request, pk=None):
        try:
            player = Players.objects.get(pk=pk)
            serializer = UsersSerializer(player, context={'request': request})
            return Response(serializer.data)
        except Exception as ex:
            return HttpResponseServerError(ex)

    def list(self, request):
        players = Players.objects.all()
        serializer = UsersSerializer(
            players, many=True, context={'request': request})
        return Response(serializer.data)


@csrf_exempt
def register_user(request):

    # incoming Json string
    req_body = json.loads(request.body.decode())

    # check if user exists in db
    user_exists = User.objects.filter(email=req_body['email']).exists()

    if user_exists:
        data = json.dumps({"msg": "user already exists"})
        return HttpResponse(data, content_type='application/json')

    # invoke Djangos built in user model
    new_user = User.objects.create_user(
        username=req_body['username'],
        email=req_body['email'],
        password=req_body['password'],
        first_name=req_body['first_name'],
        last_name=req_body['last_name'],
        is_active=True,
        is_staff=False
    )

    # Add extra info to RareUsers table
    player = Players.objects.create(
        name=req_body['name'],
        age=req_body['age'],
        user=new_user
    )

    # Commit the user to the database by saving it
    player.save()

    # Use the REST Framework's token generator on the new user account
    token = Token.objects.create(user=new_user)

    # Return the token to the client
    data = json.dumps({"token": token.key})
    return HttpResponse(data, content_type='application/json')


@csrf_exempt
def login_user(request):
    # the request data
    req_body = json.loads(request.body.decode())

    # Using Django native auth
    if request.method == 'POST':
        username = req_body['username']
        password = req_body['password']
        authenticated_user = authenticate(username=username, password=password)

        # If authentication was successful, respond with their token
        if authenticated_user is not None:

            try:
                token = Token.objects.get(user=authenticated_user)
                data = json.dumps({"valid": True, "token": token.key})
                return HttpResponse(data, content_type='application/json')
            except:
                data = json.dumps(
                    {"valid": False, "msg": "There was a server error when logging in the user"})
                return HttpResponse(data, content_type='application/json')

        else:
            # Bad login details were provided. So we can't log the user in.
            data = json.dumps({"valid": False})
            return HttpResponse(data, content_type='application/json')


@csrf_exempt
def get_current_user(request):

    req_body = json.loads(request.body.decode())

    try:
        user_id = Token.objects.get(key=req_body['token']).user_id
        data = json.dumps({"user_id": user_id})
        return HttpResponse(data, content_type="application/json")
    except Token.DoesNotExist:
        data = json.dumps(
            {"valid": False, "msg": "No currently authenticated user."})
        return HttpResponse(data, content_type='application/json')
