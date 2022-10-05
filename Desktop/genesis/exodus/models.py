import email
from tkinter import CASCADE
from django.db import models
from django.utils import timezone

# Create your models here.
GENRE_CHOICES = [
    ('RAP', 'RAP'),
    ('H-H', 'HIPHOP'),
    ('CM', 'CLASSICAL-MUSIC'),
    ('POP', 'POP'),
    ('HR', 'HARD-ROCK')
]



# class Person(models.Model):
#     first_name = models.CharField(max_length=30)
#     last_name = models.CharField(max_length=30)
#     genre_choice = models.CharField(choices=GENRE_CHOICES, max_length=3)

# class Musician(models.Model):
#     first_name = models.CharField(max_length=40)
#     last_name = models.CharField(max_length=40)
#     instrument = models.CharField(max_length=60)


# class Album(models.Model):
#     artist = models.CharField(max_length=25, null=True)
#     name = models.CharField(max_length=40)
#     release_date = models.DateField(blank=True)
#     number_of_stars = models.IntegerField()

#now to work on relationships

# class Manufacturer(models.Model):
    #...
#   pass

#class Car(models.Model):
 #   manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE, related_name='manufacturer')
    # using the Many to one-ForiegnKey, the attribute which holds the link should be nested within the 'Many'
    # relative. 
    # That way it can be edited.

#class Topping(models.Model):
 #   pass

#class Pizza(models.Model):
   # toppings = models.ManyToManyField(Topping)
    # for the many to many relationships the attribute that bears the link should be nested within the 'Many' 
    # relationship to be edited
    # and it should not be stated more than once


#class Publication(models.Model):
 #   title = models.CharField(max_length=80)

  #  class Meta:
   #     ordering = ['title']

    #def __str__(self):
     #   return self.title


# class Article(models.Model):
#     publications = models.ManyToManyField(Publication)
#     headline = models.CharField(max_length=100)

#     class Meta:
#         ordering = ['headline']
#     def __str__(self):
#         return self.headline


class Reporter(models.Model):
    first_name= models.CharField(max_length=40)
    last_name = models.CharField(max_length=40)
    email_address = models.EmailField(null=True)

    def __str__(self):
        return (self.first_name, self.last_name)


class Article(models.Model):
    headline = models.CharField(max_length=100)
    reporter = models.ForeignKey(Reporter, on_delete=models.CASCADE, null=True)
    pub_date = models.DateField(default=timezone.now)


    def __str__(self):
        return self.headline

    class Meta:
        ordering = ['headline']