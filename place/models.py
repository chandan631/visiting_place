from django.db import models

class State(models.Model):
    name = models.CharField( max_length=100 , unique=True )
    def __str__(self):
        return self.name

class District(models.Model):
    name = models.CharField( max_length=100 , unique=True )
    state = models.ForeignKey(State, related_name='districts', on_delete=models.CASCADE)
    def __str__(self):
        return f"{self.name}, {self.state.name}"

class VisitingPlace(models.Model):
    name = models.CharField( max_length=100 , unique=True )
    district = models.ForeignKey(District, related_name='visiting_places', on_delete=models.CASCADE)
    popularity = models.IntegerField(default=0)
    image = models.ImageField(upload_to='visiting_places/', null=True, blank=True)
    def __str__(self):
        return self.name
