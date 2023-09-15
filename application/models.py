from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
  name = models.CharField(max_length=255)

  class Meta:
    ordering = ('name',)
    verbose_name_plural = 'Categories'
    
  def __str__(self):
    return self.name
  
class Application(models.Model):
    class AppStates(models.IntegerChoices):
       ACCEPTED = 1
       DECLINED = 2
       PENDING = 3
    class Universities(models.TextChoices):
      BUET = "BUET"
      DUET = "DUET"
      RUET = "RUET"
      CUET = "CUET"
      KUET = "KUET"
      SEC = "SEC"
      MIST = "MIST"
      MEC = "MEC"
      IUT = "IUT"
    
    appuniname = models.TextField(choices=Universities.choices)
    appstate = models.IntegerField(choices=AppStates.choices, default=3)
    message = models.TextField(blank=True, null=True)
    created_by = models.ForeignKey(User, related_name='applications', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        string = "From student:" + self.created_by.username + ", For: " + self.appuniname
        return string
