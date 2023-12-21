from django.db import models

class Driver(models.Model):
    driver_name = models.CharField(max_length=100)
    age = models.IntegerField(default=1)
    birthplace = models.CharField(max_length=100)
    team = models.CharField(max_length=100)

    def __str__(self):
        return f'<Driver:id={self.id}, name={self.driver_name}, age={self.age}, birthplace={self.birthplace}, team={self.team}>'

class Qualifying(models.Model):
    year = models.IntegerField(default=2023)
    gp = models.CharField(max_length=100)
    rank = models.IntegerField(default=1)
    driver = models.ForeignKey(Driver, on_delete=models.CASCADE)

    def __str__(self):
        return f'<Qualifying:id={self.id}, year={self.year},gp={self.gp}, driver={self.driver.driver_name}, rank={self.rank}>'

class Final(models.Model):
    year = models.IntegerField(default=2023)
    gp = models.CharField(max_length=100)
    rank = models.IntegerField(default=1)
    driver = models.ForeignKey(Driver, on_delete=models.CASCADE)

    def __str__(self):
        return f'<Final:id={self.id}, year={self.year},gp={self.gp}, driver={self.driver.driver_name}, rank={self.rank}>'

class Point(models.Model):
    year = models.IntegerField(default=2023)
    gp = models.CharField(max_length=100)
    point = models.IntegerField(default=1)
    rank = models.IntegerField(default=1)
    driver = models.ForeignKey(Driver, on_delete=models.CASCADE)

    def __str__(self):
        return f'<Final:id={self.id}, year={self.year},gp={self.gp}, driver={self.driver.driver_name}, point={self.point},rank={self.rank}>'
    
