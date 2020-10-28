from django.db import models
from datetime import datetime

class Image_data(models.Model):
    image = models.FileField()
    prediction = models.CharField(max_length=152)
   # date = datetime
    
    def __str__(self):
        return self.image
    
