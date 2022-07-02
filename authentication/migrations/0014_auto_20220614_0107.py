# Generated by Django 3.2.13 on 2022-06-13 19:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0013_alter_profile_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='FavMovieField',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('field', models.CharField(choices=[('All', 'All'), ('Action', 'Action'), ('Comedy', 'Comedy'), ('Drama', 'Drama'), ('Fantasy', 'Fantasy'), ('Horror', 'Horror'), ('Mystery', 'Mystery'), ('Romance', 'Romance'), ('Thriller', 'Thriller'), ('Musical', 'Musical'), ('Musical', 'Musical')], default='All', max_length=16, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='FavMusicField',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('field', models.CharField(choices=[('All', 'All'), ('Country', 'Country'), ('Classical', 'Classical'), ('Dance', 'Dance'), ('Blues', 'Blues'), ('Drill', 'Drill'), ('DnB', 'DnB'), ('Dubstep', 'Dubstep'), ('Electronic', 'Electronic'), ('Folk', 'Folk'), ('Funk', 'Funk'), ('Garage', 'Garage'), ('Indie', 'Indie'), ('Hiphop', 'Hiphop'), ('House', 'House'), ('Metal', 'Metal'), ('Jazz', 'Jazz'), ('Kpop', 'Kpop'), ('Pop', 'Pop'), ('Punk', 'Punk'), ('Psychedelic', 'Psychedelic'), ('Rap', 'Rap'), ('Rock', 'Rock'), ('RnB', 'RnB'), ('Reggae', 'Reggae'), ('Soul', 'Soul')], default='All', max_length=16, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='UnFavMovieField',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('field', models.CharField(choices=[('All', 'All'), ('Action', 'Action'), ('Comedy', 'Comedy'), ('Drama', 'Drama'), ('Fantasy', 'Fantasy'), ('Horror', 'Horror'), ('Mystery', 'Mystery'), ('Romance', 'Romance'), ('Thriller', 'Thriller'), ('Musical', 'Musical'), ('Musical', 'Musical')], max_length=16, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='UnFavMusicField',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('field', models.CharField(choices=[('All', 'All'), ('Country', 'Country'), ('Classical', 'Classical'), ('Dance', 'Dance'), ('Blues', 'Blues'), ('Drill', 'Drill'), ('DnB', 'DnB'), ('Dubstep', 'Dubstep'), ('Electronic', 'Electronic'), ('Folk', 'Folk'), ('Funk', 'Funk'), ('Garage', 'Garage'), ('Indie', 'Indie'), ('Hiphop', 'Hiphop'), ('House', 'House'), ('Metal', 'Metal'), ('Jazz', 'Jazz'), ('Kpop', 'Kpop'), ('Pop', 'Pop'), ('Punk', 'Punk'), ('Psychedelic', 'Psychedelic'), ('Rap', 'Rap'), ('Rock', 'Rock'), ('RnB', 'RnB'), ('Reggae', 'Reggae'), ('Soul', 'Soul')], max_length=16, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='profile',
            name='disliked_movie_genres',
            field=models.ManyToManyField(to='authentication.UnFavMovieField'),
        ),
        migrations.AddField(
            model_name='profile',
            name='disliked_music_genres',
            field=models.ManyToManyField(to='authentication.UnFavMusicField'),
        ),
        migrations.AddField(
            model_name='profile',
            name='favourite_movie_genres',
            field=models.ManyToManyField(to='authentication.FavMovieField'),
        ),
        migrations.AddField(
            model_name='profile',
            name='favourite_music_genres',
            field=models.ManyToManyField(to='authentication.FavMusicField'),
        ),
    ]
