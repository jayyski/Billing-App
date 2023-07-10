from django.db import models

# Create your models here.
class Bill(models.Model):
    date = models.DateField()
    bill_name = models.CharField(max_length=100)
    amount = models.DecimalField(max_digits=8, decimal_places=2)

    class Meta:
        db_table = "Bills"
        ordering = ['date']