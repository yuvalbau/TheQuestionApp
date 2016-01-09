from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.contrib.auth.models import User


@python_2_unicode_compatible
class Question(models.Model):
    title=models.CharField(max_length=200)
    description=models.CharField(max_length=200)
    author=models.ForeignKey(User)  
    
    def __str__(self):
        return self.title    
    
        
    def as_json(self):
        return dict(title = self.title,
             description = self.description,
             author = self.author.id,
             author_name = self.author.username,
             question_id=self.pk)


    def getQid(self):
        return self.pk