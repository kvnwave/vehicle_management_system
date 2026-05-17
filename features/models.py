from django.db import models

class Vehicle(models.Model):
    name = models.CharField(max_length=50)
    price = models.FloatField()

    def vehicle_info(self):
        return f"{self.name} costs {self.price}"

class Car(Vehicle):
    doors = models.IntegerField()

    def vehicle_info(self):
        return f"{self.name} Car with {self.doors} doors costs {self.price}"

class Motorcycle(Vehicle):
    helmet_included = models.BooleanField()

    def vehicle_info(self):
        if self.helmet_included == True:
            return f"{self.name} Motorcycle with helment costs {self.price}"
        else: 
            return f"{self.name} Motorcycle without helment costs {self.price}"


    
