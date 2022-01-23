from datetime import datetime
from django.db import models
from datetime import datetime

# Create your models here.
class count_user(models.Model):
    username=models.CharField(max_length=50)
    count=models.IntegerField()
    loginAt=models.DateTimeField(default=datetime.now())
