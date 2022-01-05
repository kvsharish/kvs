from django.db import models
from django.db import models
class items(models.Model):
    name=models.CharField(max_length=40)
    description=models.TextField()
    costperitem=models.BigIntegerField()
    stockquantity=models.BigIntegerField()
    volume=models.DecimalField(max_digits=89, decimal_places=2, blank=True, null=True)


    def get_volume(self):
        volume=self.costperitem*self.stockquantity
        return volume
    def save(self, *args, **kwargs):
        self.volume=self.get_volume()
        super(items, self).save()
    def __str__(self):
        return self.name
# Create your models here.
