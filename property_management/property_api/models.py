from django.db import models


class Building(models.Model):

    building_id = models.AutoField(primary_key=True)
    building_name = models.CharField(max_length=50, unique=True)
    building_address = models.CharField(max_length=500)
    building_landmark = models.CharField(max_length=255)

    class Meta:
        ordering = ['building_id']


class Room(models.Model):

    BHK_1 = 'BHK_1'
    BHK_2 = 'BHK_2'
    BHK_3 = 'BHK_3'
    STUDIO = 'STUDIO'

    TYPE_CHOICES = (
        (BHK_1, '1 BHK'),
        (BHK_2, '2 BHK'),
        (BHK_3, '3 BHK'),
        (STUDIO, 'Studio')
    )

    room_id = models.AutoField(primary_key=True)
    flat_number = models.CharField(max_length=20, unique=True)
    rent = models.PositiveIntegerField(default=0)
    number_of_bathroom = models.PositiveIntegerField(default=0)
    maintenance = models.PositiveIntegerField(default=0)
    type = models.CharField(max_length=16, choices=TYPE_CHOICES)
    building = models.ForeignKey(Building, on_delete=models.CASCADE)

    class Meta:
        ordering = ['room_id']

    @property
    def building_details(self):
        return self.building
