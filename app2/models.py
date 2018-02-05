# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
import json
from datetime import datetime
# Create your models here.
choices = [('18k', '18k'), ('17k', '17k'), ('16k', '16k'), ('15k', '15k'), ('14k', '14k'),
           ('13k', '13k'), ('12k', '12k'), ('11k', '11k'), ('10k', '10k'), ('9k', '9k'),
           ('8k', '8k'), ('7k', '7k'), ('6k', '6k'), ('5k', '5k'), ('4k', '4k'),
           ('3k', '3k'), ('2k', '2k'), ('1k', '1k'), ('1d', '1d'), ('2d', '2d'), ('3d', '3d'),
           ('4d', '4d'), ('5d', '5d'), ('6d', '6d'), ('7d', '7d'), ('8d', '8d'), ('9d', '9d'), ('10d', '10d')]
class UserInfo(models.Model):
    username = models.CharField(max_length=20,unique=True)
    password = models.CharField(max_length=20)
    age = models.SmallIntegerField(default=0)
    strength = models.CharField(max_length=4,default='18k',choices=choices)
    description = models.CharField(max_length=200,default="")
    email = models.CharField(max_length=128)
    def __unicode__(self):
        return self.username+" strength:"+self.strength+" dcp:"+self.description
class GameInfo(models.Model):
    player1 = models.ForeignKey(UserInfo,related_name='player1')
    player2 = models.ForeignKey(UserInfo,related_name='player2')
    create_datetime = models.DateTimeField(default=datetime.now())
    # who is black
    Black = models.CharField(max_length=2,default="1",choices=[('1','player1'),('2','player2')])
    Founder = models.CharField(max_length=2,default="1",choices=[('1','player1'),('2','player2')])
    p1_message = models.TextField(default='',max_length=800)
    p2_message = models.TextField(default='',max_length=800)
    steps = models.CharField(max_length=2500)
    def setSteps(self,x):
        self.steps=json.dumps(x)
    def getSteps(self):
        return json.loads(self.steps)
    def __unicode__(self):
        return self.player1.username+" "+self.player2.username+str(self.create_datetime)

class UserHomeMessage(models.Model):
    message_type = models.CharField(max_length=10,choices=(
        ('inviting','is inviting'),('invited','is invited'),('accepted','\'s invitation is accept')))
    from_user = models.ForeignKey(UserInfo)
    to_user = models.ForeignKey(UserInfo,related_name="to_user")
    def __unicode__(self):
        return self.from_user.username+" is "+self.message_type+" "+self.to_user.username

class OnlineUserList(models.Model):
    user = models.OneToOneField(UserInfo)
    state = models.CharField(max_length=1,choices=[('r','ready'),('b','busy'),('r','rest')])
    def __unicode__(self):
        return self.user.username+":"+self.state

class GameMessage(models.Model):
    game_id = models.OneToOneField(GameInfo)
    black =models.BooleanField(default=True)
    info = models.CharField(max_length=5)
    def __unicode__(self):
        if self.black:
            b='B'
        else:
            b='W'
        return "gameId:"+str(self.game_id.id)+":"+b+self.info

