from django.db import models
from cloudinary.models import CloudinaryField
# Create your models here.

class Post(models.Model):
    class Meta(object):
        db_table='posts'

    name = models.CharField(
        'Name', blank=False, max_length=14, null=False, db_index=True, default='Anonimus'
        )
    body = models.CharField(
            'Body', blank=True, null=True, max_length=140, db_index=True
        )
    like = models.IntegerField(
        'like', blank = True, null=True, default=0
        )
    photo = CloudinaryField(
        'photo', blank= True, null=True
        )
    created_at = models.DateField(
            'Created DateTime', blank=True, auto_now_add=True
        )
