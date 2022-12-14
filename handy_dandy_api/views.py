from .models import User, Task
from rest_framework import generics
from .serializers import UserSerializer, TaskSerializer
from functools import wraps
import jwt
from django.http import JsonResponse
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
import json
from django.db.models import Q


class UserList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


def get_token_auth_header(request):
    """Obtains the Access Token from the Authorization Header
    """
    auth = request.META.get("HTTP_AUTHORIZATION", None)
    parts = auth.split()
    token = parts[1]

    return token


def requires_scope(required_scope):
    """Determines if the required scope is present in the Access Token
    Args:
        required_scope (str): The scope required to access the resource
    """
    def require_scope(f):
        @wraps(f)
        def decorated(*args, **kwargs):
            token = get_token_auth_header(args[0])
            decoded = jwt.decode(token, verify=False)
            if decoded.get("scope"):
                token_scopes = decoded["scope"].split()
                for token_scope in token_scopes:
                    if token_scope == required_scope:
                        return f(*args, **kwargs)
            response = JsonResponse(
                {'message': 'You don\'t have access to this resource'})
            response.status_code = 403
            return response
        return decorated
    return require_scope


@api_view(['POST'])
def get_user(request):
    try:
        parsed_req = json.loads(request.body)
        user = User.objects.get(sid=parsed_req["sid"])
        tasks = user.task_set.all()
        tasks_serializer = TaskSerializer(tasks, many=True)
        serializer = UserSerializer(user)
        if user:

            return Response([serializer.data, tasks_serializer.data])

    except:
        response = Response('User not found')
        response.status_code = 404

        return response


@api_view(['POST'])
def get_pros(request):
    try:
        parsed_req = json.loads(request.body)
        pros = User.objects.filter(
            Q(zip=parsed_req["zip"]) & Q(is_pro=True))
        pro_serializer = UserSerializer(pros, many=True)

        if pros:

            return Response(pro_serializer.data)

    except:
        response = Response('User not found')
        response.status_code = 404

        return response


@api_view(['POST'])
def create_user(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    else:
        return Response(serializer.errors)


@api_view(['POST'])
def create_task(request):
    serializer = TaskSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    else:
        return Response(serializer.errors)


@api_view(['POST'])
def update_task(request):
    parsed_req = json.loads(request.body)
    task = Task.objects.get(id=parsed_req["id"])
    data = TaskSerializer(instance=task, data=request.data)
    if data.is_valid():
        data.save()
        return Response(data.data)
    else:
        return Response(data.errors)


@api_view(['POST'])
def delete_task(request):
    parsed_body = json.loads(request.body)
    task = Task.objects.get(id=parsed_body["id"])
    task.delete()

    return JsonResponse({'message': 'DELETED'})


class TaskList(generics.ListAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer


class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class TaskDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer


# test endpoints


@api_view(['GET'])
@permission_classes([AllowAny])
def public(request):
    return JsonResponse({'message': 'Hello from a public endpoint! You don\'t need to be authenticated to see this.'})


@api_view(['GET'])
@requires_scope('read:messages')
def private_scoped(request):
    return JsonResponse({'message': 'Hello from a private endpoint! You need to be authenticated and have a scope of read:messages to see this.'})
