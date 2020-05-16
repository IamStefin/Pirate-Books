from django.db import models
import os
from django.conf import settings
# Create your models here.

class SubmitBook(models.Model):
    title = models.CharField(max_length=255)
    document = models.FileField(upload_to='books/')
    author = models.CharField(max_length=255,null=True)
    approved = models.BooleanField(default=False)
    uploaded_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        
        return str(self.title)

    def delete(self):
        print(settings.MEDIA_ROOT)
        try:
            os.remove(str(settings.MEDIA_ROOT)+"/"+str(self.document))
            super().delete()
        except:
            print("err")
