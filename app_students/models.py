from django.db import models
# Create your models here.
class GoogleSheetData(models.Model):
    D = models.IntegerField()
    email = models.EmailField()
    years = models.IntegerField(null=True, blank=True)
    student_id = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    nickname = models.CharField(max_length=255)
    gender = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    def __str__(self):
        return self.name
    