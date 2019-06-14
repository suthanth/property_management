from rest_framework import serializers

from property_management.property_api.models import Building, Room


class BuildingSerializer(serializers.ModelSerializer):

    class Meta:
        model = Building
        fields = ('building_id', 'building_name', 'building_address', 'building_landmark')

    def create(self, validated_data):
        instance = Building.objects.create(
            building_name=validated_data['building_name'],
            building_address=validated_data['building_address'],
            building_landmark=validated_data['building_landmark']
        )
        return instance

    def update(self, instance, validated_data):
        instance.building_name = validated_data['building_name']
        instance.building_address = validated_data['building_address']
        instance.building_landmark = validated_data['building_landmark']

        instance.save()
        return instance


class RoomSerializer(serializers.ModelSerializer):
    building_details = BuildingSerializer(read_only=True)

    class Meta:
        model = Room
        fields = ('room_id', 'flat_number', 'rent', 'number_of_bathroom',
                  'maintenance', 'type', 'building', 'building_details')

    def create(self, validated_data):
        building = Building.objects.get(building_id=validated_data['building'])
        instance = Room.objects.create(
            flat_number=validated_data['flat_number'],
            rent=validated_data['rent'],
            number_of_bathroom=validated_data['number_of_bathroom'],
            maintenance=validated_data['maintenance'],
            type=validated_data['type'],
            building=building
        )
        return instance

    def update(self, instance, validated_data):
        instance.rent = validated_data['rent']
        instance.maintenance = validated_data['maintenance']

        instance.save()
        return instance
