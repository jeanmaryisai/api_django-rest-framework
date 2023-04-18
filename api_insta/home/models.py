from django.db import models

# Create your models here.
class Stats(models.Model):
    date=models.DateField()
    rutshelle=models.IntegerField()
    darlinedesca=models.IntegerField()
    vanessa_desireofficiel=models.IntegerField()
    fatiful=models.IntegerField()
    aniealerte=models.IntegerField()
    tafaayiti=models.IntegerField()
    bedjineofficiel=models.IntegerField()
    blondedyferdinandshop=models.IntegerField()

    class Meta:
        ordering = ('-date',)
    
    def __str__(self):
        return str(self.date)