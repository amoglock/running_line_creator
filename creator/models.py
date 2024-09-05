from django.db import models

class Video(models.Model):
    text = models.CharField(max_length=100)
    pub_date = models.DateTimeField("date published")
    file = models.FileField(upload_to="files/")

    def __str__(self):
        return self.text