from django.db import models

STATE = (
    ('IN','Interno'),
    ('EX','Externo'),
    )

# Create your models here.
class Extorsion(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    phone = models.IntegerField()
    description = models.TextField()
    state = models.CharField(choices=STATE, max_length=50)
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return "%s %s" % ("Numero reportado:", self.phone)