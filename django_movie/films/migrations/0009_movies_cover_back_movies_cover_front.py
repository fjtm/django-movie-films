# Generated by Django 5.0 on 2024-01-04 12:40

import films.models
from django.db import migrations, models

def populate_cover_fields(apps, schema_editor):
    Movies = apps.get_model('films', 'Movies')
    for movie in Movies.objects.all():
        movie.cover_front = f'covers/{movie.img_front}.jpg'
        movie.cover_back = f'covers/{movie.img_back}.jpg'
        movie.save()

class Migration(migrations.Migration):

    dependencies = [
        ('films', '0008_remove_movies_cover_back_remove_movies_cover_front_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='movies',
            name='cover_back',
            field=models.ImageField(null=True, upload_to=films.models.get_img_back_upload_path),
        ),
        migrations.AddField(
            model_name='movies',
            name='cover_front',
            field=models.ImageField(null=True, upload_to=films.models.get_img_front_upload_path),
        ),
        migrations.RunPython(populate_cover_fields),
    ]
