from django.db import models
import random as rd
import os

class Base:
    number_of_ship = 3

class Board(models.Model):
    number_of_player = 2
    code = models.IntegerField(default=-1)
    num_player = models.IntegerField(default=0)
    turn = models.IntegerField(default=0)
    status = models.BooleanField(default=False)
    winner = models.CharField(max_length=100, default="")
    
class Update(models.Model):
    name = models.CharField(max_length=100, default="")
    front = models.IntegerField(default=1)
    change = models.IntegerField(default=0)
    board = models.ForeignKey(Board, on_delete=models.CASCADE)
    
class Player(models.Model):
    name = models.CharField(max_length=100)
    front = models.IntegerField(default=1)
    board = models.ForeignKey(Board, on_delete=models.CASCADE)
    survive = models.IntegerField(default=Base.number_of_ship)
    
class Ship(models.Model):
    number = models.IntegerField()
    Hp = models.IntegerField()
    Atk = models.IntegerField()
    owner = models.ForeignKey(Player, on_delete=models.CASCADE)
    board = models.ForeignKey(Board, on_delete=models.CASCADE)
    



