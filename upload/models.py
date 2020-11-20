from django.db import models

# Create your models here.
class Animal(models.Model):
    DOG = 'Dog'
    CAT = 'Cat'
    OTHER = 'Other'
    SPECIES_CHOICES = (
        (DOG, 'Dog'),
        (CAT, 'Cat'),
        (OTHER, 'Other'),
    )
    YES = 'Yes'
    NO = 'No'
    NEUTERED_CHOICES = (
        (YES,'Yes'),
        (NO,'No'),
    )
    species = models.CharField(max_length = 20,choices = SPECIES_CHOICES,default = OTHER) 
    name = models.CharField(max_length = 200,null = True)
    breed = models.CharField(max_length = 200,null = True)
    color = models.CharField(max_length = 50,null = True)
    gender = models.CharField(max_length = 20,null = True)
    size = models.CharField(max_length = 50,null = True)
    age = models.CharField(max_length = 50,null = True)
    city = models.CharField(max_length = 50,null = True)
    reference_no = models.IntegerField(primary_key = True)
    neutered = models.CharField(max_length = 5,choices = NEUTERED_CHOICES,default = NO)
    description = models.CharField(max_length = 500,null = True)

class AnimalImages(models.Model):
    animal = models.ForeignKey(Animal, on_delete = models.CASCADE)
    image = models.ImageField(upload_to = 'images/',null = True,blank = True)

class Volunteer(models.Model):
    id = models.IntegerField(primary_key = True)
    name = models.CharField(max_length = 200,null = True)
    experience = models.CharField(max_length = 20,null = True)
    species_fostered = models.CharField(max_length = 200,null = True)
    image = models.ImageField(upload_to = 'images/',null = True,blank = True)

class Stories(models.Model):
    id = models.IntegerField(primary_key = True)
    image = models.ImageField(upload_to = 'images/',null = True,blank = True)
    title = models.CharField(max_length = 50,null = True)
    summary = models.TextField(null = True)
    para1 = models.TextField(null = True)
    para2 = models.TextField(null = True)
    para3 = models.TextField(null = True)
    para4 = models.TextField(null = True)

class Contact(models.Model):
    name = models.CharField(max_length = 100,null = True)
    email = models.CharField(max_length = 100,null = True)
    message = models.TextField(null = True)
