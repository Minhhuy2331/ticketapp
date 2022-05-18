from django.contrib import admin
from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register(prefix='users', viewset=views.UserViewSet, basename='user')
router.register(prefix='Tickets', viewset=views.TicketViewSet, basename='Ticket')
router.register(prefix='Buses', viewset=views.TuyenXeViewSet, basename='Buses')
router.register(prefix='Cars', viewset=views.CarViewSet, basename='Car')
router.register(prefix='Ticket_details', viewset=views.Ticket_detailsViewSet, basename='Ticket_details')
# router.register(prefix='comments', viewset=views.CommentViewSet, basename='comment')

urlpatterns = [
    path('', include(router.urls)),
]