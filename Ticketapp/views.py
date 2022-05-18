from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import viewsets, generics, status, permissions, mixins
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import *
from .perms import CommentOwnerPerms
from .serializers import *


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


class TicketViewSet(viewsets.ViewSet, generics.CreateAPIView, generics.ListAPIView):
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer


class TuyenXeViewSet(viewsets.ViewSet, generics.CreateAPIView, generics.ListAPIView):
    queryset = Buses.objects.all()
    serializer_class = BusesSerializer


class CarViewSet(viewsets.ViewSet, generics.CreateAPIView, generics.ListAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer


class Ticket_detailsViewSet(viewsets.ViewSet, generics.CreateAPIView, generics.ListAPIView):
    queryset = Ticket_details.objects.all()
    serializer_class = Ticket_detailsSerializer