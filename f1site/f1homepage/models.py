from django.db import models

class Qualifying (models.Model):
    venue = models.CharField(max_length=100)
    rank = models.IntegerField(default=1)
    driver_name = models.CharField(max_length=100)

    def __str__(self):
     return'<Qualifyinz:id=' + str(self.id) + ','+ \
      self.venue+self.driver_name+'('+str(self.rank)+')>'
# Create your models here.
