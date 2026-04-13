from django.db import models

 #Create your models here.



class Book(models.Model):

    title=models.CharField(max_length=200,null=True)

    price=models.IntegerField(null=True)


    def __str__(self):

        return '{}'.format(self.title)