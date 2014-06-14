from django.db import models
from django import forms
from django.forms import ModelForm

from django.contrib.auth.models import User


class DataSet(models.Model):
    """The dataset holds the collection of videos that will
    be analyzed as a group."""
    name = models.CharField(max_length=120)
    creator = models.ForeignKey(User)

class DataSetForm(ModelForm):
    class Meta:
        model = DataSet
        exclude = ["creator"]


class Video(models.Model):
    """The full video that is uploaded to Kaltura"""
    filename = models.CharField(max_length=500)
    k_video_entry = models.CharField(max_length=40)
    dataset = models.ForeignKey(DataSet)

class Query(models.Model):
    """A query term made against the clip database"""
    term = models.CharField(max_length=120)
    dataset = models.ForeignKey(DataSet)

class QueryForm(ModelForm):
    class Meta:
        model = Query
        exclude = ["dataset"]

class QueryResult(models.Model):
    """All of the video hit for a query"""
    k_video_id = models.IntegerField()
    # the seconds from start where the term was found
    hit_time = models.IntegerField()
    query = models.ForeignKey(Query)


class Collection(models.Model):
    """A user curated collection of videos, from a given query"""
    name = models.CharField(max_length=120)
    dataset = models.ForeignKey(DataSet)


class Clip(models.Model):
    start = models.IntegerField()
    end = models.IntegerField()
    video = models.ForeignKey(Video)




