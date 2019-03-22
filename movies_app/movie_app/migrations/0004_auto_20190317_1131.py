# Generated by Django 2.1.7 on 2019-03-17 10:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie_app', '0003_auto_20190317_1047'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='characters',
            field=models.ManyToManyField(blank=True, to='movie_app.Character'),
        ),
        migrations.AlterField(
            model_name='movie',
            name='director',
            field=models.ManyToManyField(blank=True, to='movie_app.Director'),
        ),
    ]