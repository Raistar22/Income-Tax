from django.db import models
from django.contrib.auth.models import User

class TaxSlab(models.Model):
    year = models.IntegerField()
    regime=models.charField(max_length=20)
    slab_start = models.IntegerField()
    slab_end = models.IntegerField()
    rate = models.FloatField()

    
    def __str__(self):
        return f"{self.year} {self.regime} - {self.slab_start} to {self.slab_end}: {self.rate}%"

class Deduction(models.Model):
    name = models.CharField(max_length=50)
    max_limit = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name

class TaxPlan(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    income = models.FloatField(max_digits=12, decimal_places=2)
    year = models.IntegerField(max_length=4)
    slab_type = models.CharField(max_length=10, choices=[('old', 'Old Regime'), ('new', 'New Regime')])
    deductions = models.JSONField(default=dict)
    calculated_tax = models.DecimalField(max_digits=12, decimal_places=2)
    tax=models.FloatField()

    def __str__(self):
        return f"Tax Plan for {self.user.username} - {self.year}"

