from django.db import models


class Project (models.Model):
    objects = models.Manager()
    name = models.CharField(max_length=300, null=True)
    department = models.CharField(max_length=300, null=True)
    price = models.DecimalField(max_digits=12, decimal_places=0, null=True)
    consultant = models.CharField(max_length=300, null=True)
    owner = models.CharField(max_length=300, null=True)
    start_date = models.DateField(null=True)
    end_date = models.DateField(null=True)

    def __str__(self):
        return self.name
