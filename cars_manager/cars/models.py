from django.db import models, transaction

class Car(models.Model):
    name = models.CharField(max_length=255)
    color = models.CharField(max_length=50)
    position = models.PositiveIntegerField(unique=True)
    
    def move_to_position(self, new_position):
        """ Moves the car to a new position and reorders efficiently. """
        with transaction.atomic():
            # Ensure new position is unique by adjusting other cars
            if Car.objects.filter(position=new_position).exists():
                Car.objects.filter(position__gte=new_position).update(position=models.F('position') + 1)

            # Assign the new position
            self.position = new_position
            self.save()

    class Meta:
        ordering = ['position']
