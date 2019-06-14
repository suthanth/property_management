from rest_framework import generics
from rest_framework import status
from rest_framework.response import Response

from property_management.property_api.models import Building, Room
from property_management.property_api.serializers import BuildingSerializer, RoomSerializer


class BuildingCreateView(generics.ListCreateAPIView):
    """
    This class is responsible for creating a Building object
    """
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


class BuildingDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    This class is responsible for fetch, update and delete a building object
    """
    queryset = Building.objects.all()
    serializer_class = BuildingSerializer

    def get(self, request, *args, **kwargs):
        try:
            application_data = self.queryset.get(building_id=kwargs['building_id'])
            building_details = BuildingSerializer(application_data).data
            return Response(
                data=building_details,
                status=status.HTTP_201_CREATED
            )
        except Building.DoesNotExist:
            return Response(
                data='Building with id {} does not exist'.format(kwargs['building_id']),
                status=status.HTTP_404_NOT_FOUND
            )

    def put(self, request, *args, **kwargs):
        try:
            serializer = BuildingSerializer()
            application_data = self.queryset.get(building_id=kwargs['building_id'])
            updated_data = serializer.update(application_data, request.data)
            building_details = BuildingSerializer(updated_data).data
            return Response(
                data=building_details,
                status=status.HTTP_200_OK
            )
        except Building.DoesNotExist:
            return Response(
                data='Building with id {} does not exist'.format(kwargs['building_id']),
                status=status.HTTP_404_NOT_FOUND
            )

    def delete(self, request, *args, **kwargs):
        try:
            application_data = self.queryset.get(building_id=kwargs['building_id'])
            application_data.delete()
            return Response(
                data='Building deleted successfully',
                status=status.HTTP_204_NO_CONTENT
            )
        except Building.DoesNotExist:
            return Response(
                data='Building with id {} does not exist'.format(kwargs['building_id']),
                status=status.HTTP_404_NOT_FOUND
            )


class RoomCreateView(generics.ListCreateAPIView):
    """
    This class is responsible for creating a Room object
    """
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


class RoomDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    This class is responsible for fetch, update and delete a Room object
    """
    queryset = Room.objects.all()
    serializer_class = RoomSerializer

    def get(self, request, *args, **kwargs):
        try:
            application_data = self.queryset.get(room_id=kwargs['room_id'])
            room_details = RoomSerializer(application_data).data
            return Response(
                data=room_details,
                status=status.HTTP_200_OK
            )
        except Room.DoesNotExist:
            return Response(
                data='Room with id {} does not exist'.format(kwargs['room_id'])
            )

    def put(self, request, *args, **kwargs):
        try:
            serializer = RoomSerializer()
            application_data = self.queryset.get(room_id=kwargs['room_id'])
            updated_data = serializer.update(application_data, request.data)
            room_details = RoomSerializer(updated_data).data
            return Response(
                data=room_details,
                status=status.HTTP_200_OK
            )
        except Room.DoesNotExist:
            return Response(
                data='Room with id {} does not exist'.format(kwargs['room_id'])
            )

    def delete(self, request, *args, **kwargs):
        try:
            application_data = self.queryset.get(room_id=kwargs['room_id'])
            application_data.delete()
            return Response(
                data='Room deleted successfully',
                status=status.HTTP_204_NO_CONTENT
            )
        except Room.DoesNotExist:
            return Response(
                data='Room with id {} does not exist'.format(kwargs['room_id']),
                status=status.HTTP_204_NO_CONTENT
            )


class RoomsForEachBuildingDetailView(generics.RetrieveAPIView):
    """
    This class is responsible for fetching all Room objects for specified Building object
    """
    queryset = Room.objects.all()
    serializer_class = RoomSerializer

    def get(self, request, *args, **kwargs):
        try:
            application_data = list(Room.objects.filter(building=kwargs['building']))
            print(application_data)
            detail_view = RoomSerializer(application_data, many=True).data
            return Response(
                data=detail_view,
                status=status.HTTP_200_OK
            )

        except Building.DoesNotExist:
            return Response(
                data='Invalid building Id {}'.format(kwargs['building']),
                status=status.HTTP_404_NOT_FOUND
            )
