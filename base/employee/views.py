from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from .models import User
from rest_framework import viewsets
from .serializers import UserSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from rest_framework.authentication import SessionAuthentication


class Index(APIView):
    permission_classes = (IsAuthenticated,)
    authentication_classes = (SessionAuthentication,)


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    name = 'user-list'

    filter_backends = [
        DjangoFilterBackend,
        filters.SearchFilter,
        filters.OrderingFilter,
    ]
    filterset_fields = {
        "is_fired": ["exact", ],  # BooleanField
        "fire_date": ["date__exact", ]  # DateTimeField
    }

    def get_queryset(self):
        return User.objects.all()


def employees(request):
    employee_list = User.objects.all()
    context = {'employee': employee_list}
    return render(request, 'users.html', context)


def signup(request):
    return render(request, 'signup.html')
