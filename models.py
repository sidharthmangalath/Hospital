from django.db import models

# Create your models here.
class medi(models.Model):
    Name=models.CharField(max_length=100)
    Age=models.IntegerField()
    Address=models.CharField(max_length=500)
class doct1(models.Model):
    name=models.CharField(max_length=100)
    department=models.CharField(max_length=100)
    image=models.CharField(max_length=2500)
class dept(models.Model):
    dname=models.CharField(max_length=100)
    blockno=models.IntegerField()
class log(models.Model):
    user=models.CharField(max_length=100)
    pwd=models.CharField(max_length=100)
class apt(models.Model):
    pname=models.CharField(max_length=100)
    pmob=models.CharField(max_length=100)
    pmail=models.CharField(max_length=100)
    pdate=models.CharField(max_length=100)
    
    pdpt=models.CharField(max_length=100)
    pdtr=models.CharField(max_length=100)
    paddr=models.CharField(max_length=100)


    
