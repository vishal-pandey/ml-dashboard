from django.db import models
from django.contrib.auth.models import User

class Dataset(models.Model):
	user = models.ForeignKey(User,on_delete=models.CASCADE)
	dataset = models.FileField(upload_to='datasets',blank=False)
	def __str__(self):
	  return self.user.username


