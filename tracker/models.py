from django.db import models
from django.urls import reverse


class Expense(models.Model):
    date = models.DateField()
    description = models.CharField(max_length=1000, null=True)
    type = models.CharField(max_length=30)
    payment = models.CharField(max_length=30)
    amount = models.FloatField()
    created_by = models.CharField(max_length=100)
    created_at = models.DateField()

    class Meta:
        verbose_name = 'Expense'
        verbose_name_plural = 'Expenses'
        ordering = ['-id']

    def get_absolute_url(self):
        return reverse('tracker:expense')
