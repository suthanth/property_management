from django.urls import path

from property_management.property_api.views import BuildingCreateView, RoomCreateView

urlpatterns = [
    path('building/', BuildingCreateView.as_view(), name='Building-create-view'),
    path('room/', RoomCreateView.as_view(), name='Room-create-view'),
]
