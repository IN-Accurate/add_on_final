from django.db import models

# Create your models here.

class TitleProfile(models.Model):
    name = models.CharField(max_length =200)
    description = models.TextField()
    roll_number = models.IntegerField(help_text = "Enter a 6 digit roll number")
    last_modified = models.DateTimeField(auto_now_add = True)

    def _str_(self):
        return self.name
