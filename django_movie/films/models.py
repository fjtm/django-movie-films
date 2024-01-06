from django.db import models
import os

def get_img_front_upload_path(instance, filename):
    # Use the value of the img_front field as the filename
    filename = f"{instance.img_front}.jpg"
    print(filename)
    # Define the upload path within the /media/covers/ directory
    return os.path.join('covers', filename)
    
def get_img_back_upload_path(instance, filename):
    # Use the value of the img_front field as the filename
    filename = f"{instance.img_back}.jpg"
    # Define the upload path within the /media/covers/ directory
    return os.path.join('covers', filename)

class Movies(models.Model):
    id = models.CharField(primary_key=True,max_length=36, unique=True)
    movie_id = models.CharField(max_length=36, null=True)
    tv_serie_id = models.CharField(max_length=36, null=True)
    id_imdb = models.CharField(max_length=36, null=True)
    title = models.CharField(max_length=255, null=True)
    year = models.IntegerField(null=True)
    actors = models.TextField(null=True)
    genre = models.TextField(null=True)
    media_type = models.CharField(max_length=50, null=True)
    company = models.CharField(max_length=100, null=True)
    description = models.TextField(null=True)
    duration = models.IntegerField(null=True)
    type_film = models.CharField(max_length=50, null=True)
    img_front = models.CharField(max_length=36, null=True)
    img_back = models.CharField(max_length=36, null=True)
    url_img_front = models.ImageField(upload_to=get_img_front_upload_path, null=True)
    url_img_back = models.ImageField(upload_to=get_img_back_upload_path, null=True)

    def __str__(self):
        return self.title
