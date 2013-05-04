from django.db import models

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=128)

    def __unicode__(self):
        return self.name
    
class CV(models.Model):
    name = models.CharField(max_length=128)
    user = models.ForeignKey(User)
    
    def __unicode__(self):
        return self.name

class Section(models.Model):
    name = models.CharField(max_length=128)
    cv = models.ForeignKey(CV)
    
    def __unicode__(self):
        return "Section: " + self.name
    
class Experience(models.Model):
    name = models.CharField(max_length=128)
    type = models.CharField(max_length=128)
    description = models.CharField(max_length=256)
    from_date = models.DateField()
    to_date = models.DateField()
    user = models.ForeignKey(User)
    section = models.ForeignKey(Section)
    
    def __unicode__(self):
        return "Experience:" + self.name
    