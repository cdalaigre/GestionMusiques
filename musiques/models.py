
from django.db import models


# Create your models here.

class Artiste(models.Model):
    nom = models.CharField(max_length=64)

    def __str__(self):
        return self.nom
    
class Morceau(models.Model):
    titre = models.CharField(max_length=64)
    date_sortie = models.DateField(null=True)
    fk_artiste = models.ForeignKey(Artiste,on_delete=models.CASCADE, null=False)

    def __str__(self):
        return '{self.titre} ({self.fk_artiste.nom})'.format(self=self)
    
   
    


    