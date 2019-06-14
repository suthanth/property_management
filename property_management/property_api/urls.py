from django.urls import path

from property_management.property_api.views import BuildingCreateView, RoomCreateView, BuildingDetailView, \
    RoomDetailView

urlpatterns = [
    path('building/', BuildingCreateView.as_view(), name='Building-create-view'),
    path('building/<str:building_id>', BuildingDetailView.as_view(), name='Building-detail-view'),
    path('room/', RoomCreateView.as_view(), name='Room-create-view'),
    path('room/<str:room_id>', RoomDetailView.as_view(), name='Room-detail-view'),
]
