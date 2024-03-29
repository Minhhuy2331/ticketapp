from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import viewsets, generics, status, permissions
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import *
from .perms import CommentOwnerPerms
from .serializers import *
from django.conf import settings


class UserViewSet(viewsets.ViewSet, generics.CreateAPIView, generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get_permissions(self):
        if self.action == 'current_user':
            return [permissions.IsAuthenticated()]

        return [permissions.AllowAny()]

    @action(methods=['get'], url_path="current-user", detail=False)
    def current_user(self, request):
        return Response(self.serializer_class(request.user, context={'request': request}).data,
                        status=status.HTTP_200_OK)


class BusViewSet(viewsets.ViewSet, generics.CreateAPIView, generics.ListAPIView):
    queryset = Bus.objects.all()
    serializer_class = BusSerializer


class BusroutesViewSet(viewsets.ViewSet, generics.CreateAPIView, generics.ListAPIView):
    queryset = Busroutes.objects.all()
    serializer_class = BusroutesSerializer


class CarViewSet(viewsets.ViewSet, generics.CreateAPIView, generics.ListAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer


class Ticket_detailsViewSet(viewsets.ViewSet, generics.CreateAPIView, generics.ListAPIView):
    queryset = Ticket_details.objects.all()
    serializer_class = Ticket_detailsSerializer


class AuthInfo(APIView):
    def get(self, request):
        return Response(settings.OAUTH2_INFO, status=status.HTTP_200_OK)