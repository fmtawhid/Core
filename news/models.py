from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class postCatagory(models.Model):
    cata_name= models.CharField(max_length=100)
    cata_slug= models.SlugField()
    
    def __str__(self):
        return self.cata_name

class postmodel(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='post')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    cata_post = models.ForeignKey(postCatagory, on_delete=models.CASCADE)
    on_date = models.DateTimeField(auto_now_add=True)
    describe = models.TextField(max_length=999)

    def __str__(self):
        return self.title
