from django.db import models


class Course(models.Model):
    name = models.CharField(max_length=256)
    start_date = models.DateField()
    end_date = models.DateField()
    num_lections = models.IntegerField()

    def __str__(self):
        return self.name
