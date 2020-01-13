from django.db import models

class Book(models.Model):
	name = models.CharField(max_length=255)
	author = models.CharField(max_length=255, blank=True)
	category = models.CharField(max_length=255, default='new')
	book = models.FileField(upload_to='books/')
	audio = models.FileField(upload_to='audios/', default='wtf')
	uploaded_time = models.DateTimeField("date published")

	def __str__(self):
		return self.name

class Novel(models.Model):
	novelname = models.CharField(max_length=255)
	novelauthor = models.CharField(max_length=255, blank=True)
	novelcategory = models.CharField(max_length=255, default='new')
	novelbook = models.FileField(upload_to='books/')
	novelaudio = models.FileField(upload_to='audios/', default='wtf')
	noveluploaded_time = models.DateTimeField("date published")

	def __str__(self):
		return self.novelname

class News(models.Model):
	newsname = models.CharField(max_length=255)
	newsauthor = models.CharField(max_length=255, blank=True)
	newscategory = models.CharField(max_length=255, default='new')
	newsbook = models.FileField(upload_to='books/')
	newsaudio = models.FileField(upload_to='audios/', default='wtf')
	newsuploaded_time = models.DateTimeField("date published")

	def __str__(self):
		return self.newsname