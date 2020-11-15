from django.db import models


class Tag(models.Model):
    name = models.CharField(max_length=255)


class Video(models.Model):
    file = models.CharField(max_length=255)
    title = models.CharField(max_length=255)


class VideoTag(models.Model):
    tag = models.ForeignKey('tag', on_delete=models.CASCADE)
    video = models.ForeignKey('video', on_delete=models.CASCADE)
