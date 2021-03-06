# Generated by Django 2.1.7 on 2019-03-17 09:47

from django.db import migrations, models


class Migration(migrations.Migration):
    atomic = False
    dependencies = [
        ('movie_app', '0002_auto_20190316_1304'),
    ]

    operations = [
        migrations.CreateModel(
            name='Character',
            fields=[
                ('character_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=30)),
            ],
            options={
                'db_table': 'character',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Director',
            fields=[
                ('director_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=30)),
            ],
            options={
                'db_table': 'director',
                'ordering': ['name'],
            },
        ),
        migrations.RemoveField(
            model_name='movie',
            name='characters',
        ),
        migrations.RemoveField(
            model_name='movie',
            name='director',
        ),
        migrations.AlterField(
            model_name='movie',
            name='synopsis',
            field=models.TextField(max_length=50000),
        ),
        migrations.AddField(
            model_name='movie',
            name='characters',
            field=models.ManyToManyField(to='movie_app.Character'),
        ),
        migrations.AddField(
            model_name='movie',
            name='director',
            field=models.ManyToManyField(to='movie_app.Director'),
        ),
    ]
