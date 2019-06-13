from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework import generics

from property_management.property_api.models import Building, Room
from property_management.property_api.serializers import BuildingSerializer, RoomSerializer


class BuildingCreateView(generics.ListCreateAPIView):
    queryset = Building.objects.all()
    serializer_class = BuildingSerializer

    def post(self, request, *args, **kwargs):
        try:
            serializer = BuildingSerializer()
            application_data = serializer.create(request.data)
            building_details = BuildingSerializer(application_data).data
            return Response(
                data=building_details,
                status=status.HTTP_201_CREATED
            )

        except (KeyError, ValueError) as exception:
            return Response(
                data="failed to create Building" + str(exception),
                status=status.HTTP_400_BAD_REQUEST
            )

        except Exception as exception:
            return Response(
                data="failed to create Building" + str(exception),
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )


class RoomCreateView(generics.ListCreateAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer

    def post(self, request, *args, **kwargs):
        try:
            serializer = RoomSerializer()
            application_data = serializer.create(request.data)
            room_details = RoomSerializer(application_data).data
            return Response(
                data=room_details,
                status=status.HTTP_201_CREATED
            )

        except (KeyError, ValueError) as exception:
            return Response(
                data="failed to create Building" + str(exception),
                status=status.HTTP_400_BAD_REQUEST
            )

        except Exception as exception:
            return Response(
                data="failed to create Building" + str(exception),
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )



