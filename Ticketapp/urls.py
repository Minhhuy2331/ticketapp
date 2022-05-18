from django.contrib import admin
from django.urls import path, include
from . import views
from rest_framework import routers
from .admin import admin_site

router = routers.DefaultRouter()
router.register(prefix='users', viewset=views.UserViewSet, basename='user')
router.register(prefix='Bus', viewset=views.BusViewSet, basename='Bus')
router.register(prefix='Busroutes', viewset=views.BusroutesViewSet, basename='Busroutes')
router.register(prefix='Cars', viewset=views.CarViewSet, basename='Car')
router.register(prefix='Ticket_details', viewset=views.Ticket_detailsViewSet, basename='Ticket_details')

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin_site.urls),
]