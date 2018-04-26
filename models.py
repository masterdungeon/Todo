from django.db import models

class Todo(models.Model):
	topic = models.CharField(max_length=300)
	content = models.CharField(max_length=1000)

	def __str__(self):
		return (self.topic)
		