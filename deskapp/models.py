from django.db import models

class Desk(models.Model):
    Modalidad = models.CharField("Tipo",max_length=30)
    Precio = models.FloatField("Precio")
    TEMPO = (
        (1,"Day"),
        (2,"Week"),
        (3,"Month"),
        (4,"Semester"),
        (5,"Year")
    )
    temporalidad = models.PositiveSmallIntegerField("Temporalidad",choices=TEMPO)