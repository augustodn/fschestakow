from django.db import models

# Create your models here.


class Pharmacy(models.Model):
    name = models.CharField(max_length=200)
    phone = models.CharField(max_length=20)
    address = models.CharField(max_length=200)
    lat = models.DecimalField(max_digits=18, decimal_places=16)
    lng = models.DecimalField(max_digits=18, decimal_places=16)

    def __str__(self):
        return self.name


class Shift(models.Model):
    all_night_1 = models.ForeignKey(Pharmacy,
                                    on_delete=models.CASCADE,
                                    related_name='all_night_1')
    all_night_2 = models.ForeignKey(Pharmacy,
                                    on_delete=models.CASCADE,
                                    related_name='all_night_2')
    close_at_24 = models.ForeignKey(Pharmacy,
                                    on_delete=models.CASCADE,
                                    related_name='close_at_24')
    date = models.DateField()

    def __str__(self):
        return str(self.date)
