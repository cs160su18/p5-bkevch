from django.db import models

class Group(models.Model):
	established = models.DateTimeField(auto_now_add=True)
	name = models.CharField(max_length=50)
  
class Task(models.Model):
  name = models.CharField(max_length=50)
  start = models.DateTimeField('Start')
  end = models.DateTimeField('End')
  def __str__(self):
    return '' + self.name
  
class Tag(models.Model):
  day_choices = (
        ("Monday", 'Monday'),
        ("Tuesday", 'Tuesday'),
        ('Wednesday', 'Wednesday'),
        ('Thursday', 'Thursday'),
        ('Friday', 'Friday'), 
        ('Saturday', 'Saturday'), 
        ('Sunday', 'Sunday')
    )
  day = models.CharField(
        max_length=10,
      choices=day_choices,
        default='Monday',
  )
  description = models.CharField(max_length=30)
  #rating = models.ChoiceField(choices=['1', '2', '3', '4', '5', '6', '7', '8', '9', '10'])
  stress_choices = (
        ("1", '1'),
        ("2", '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5'), 
        ('6', '6'), 
        ('7', '7'), 
        ('8', '8'), 
        ('9', '9'), 
        ('10', '10'),
    )
  stress_rating = models.CharField(
        max_length=2,
      choices=stress_choices,
        default='5',
  )
  
  productivity_choices = (
        ("1", '1'),
        ("2", '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5'), 
        ('6', '6'), 
        ('7', '7'), 
        ('8', '8'), 
        ('9', '9'), 
        ('10', '10'),
    )
  productivity_rating = models.CharField(
        max_length=2,
      choices=productivity_choices,
        default='5',
  )
  enjoyment_choices = (
        ("1", '1'),
        ("2", '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5'), 
        ('6', '6'), 
        ('7', '7'), 
        ('8', '8'), 
        ('9', '9'), 
        ('10', '10'),
    )
  enjoyment_rating = models.CharField(
        max_length=2,
      choices=enjoyment_choices,
        default='5',
  )
  
  def __str__(self):
    return '' + self.description
  