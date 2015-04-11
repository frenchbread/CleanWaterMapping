from django.db import models

# Create your models here.


class Point(models.Model):

    Title = models.CharField(max_length=30)
    Description = models.TextField(max_length=600, )
    Address = models.CharField(max_length=100, help_text='This field is optional', blank=True)

    Latitude = models.FloatField(max_length=20, )
    Longitude = models.FloatField(max_length=100, )

    Arsenic = models.IntegerField(max_length=10, help_text='Limit - 10mg/l')
    Barium = models.IntegerField(max_length=10, help_text='Limit - 10mg/l')
    Boron = models.IntegerField(max_length=10, help_text='Limit - 2400mg/l')
    Chromium = models.IntegerField(max_length=10, help_text='Limit - 50mg/l')
    Fluoride = models.IntegerField(max_length=10, help_text='Limit - 1500mg/l')
    Selenium = models.IntegerField(max_length=10, help_text='Limit - 40mg/l')
    Uranium = models.IntegerField(max_length=10, help_text='Limit - 30mg/l')


    #water_color = models.CharField(max_length=30)
    #ph_level = models.CharField(max_length=20)
    ref_number = models.IntegerField(max_length=10, default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.Title