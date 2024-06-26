# Generated by Django 5.0.4 on 2024-05-06 19:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='driver',
            name='enjoy_cooking',
            field=models.BooleanField(default=False, verbose_name='Do you enjoy cooking at home?'),
        ),
        migrations.AddField(
            model_name='driver',
            name='enjoy_outdoor_activities',
            field=models.BooleanField(default=False, verbose_name='Do you enjoy outdoor activities like hiking or camping?'),
        ),
        migrations.AddField(
            model_name='driver',
            name='enjoy_scifi_movies',
            field=models.BooleanField(default=False, verbose_name='Are you a fan of science fiction movies?'),
        ),
        migrations.AddField(
            model_name='driver',
            name='interested_in_fitness',
            field=models.BooleanField(default=False, verbose_name='Are you interested in fitness and exercise?'),
        ),
        migrations.AddField(
            model_name='driver',
            name='morning_person',
            field=models.BooleanField(default=False, verbose_name='Are you a morning person?'),
        ),
        migrations.AddField(
            model_name='driver',
            name='pet_owner',
            field=models.BooleanField(default=False, verbose_name='Are you a pet owner?'),
        ),
        migrations.AddField(
            model_name='driver',
            name='prefer_reading_fiction',
            field=models.BooleanField(default=False, verbose_name='Do you prefer reading fiction over non-fiction?'),
        ),
        migrations.AddField(
            model_name='driver',
            name='prefer_texting_over_calling',
            field=models.BooleanField(default=False, verbose_name='Do you prefer texting over calling?'),
        ),
        migrations.AddField(
            model_name='driver',
            name='tech_savvy',
            field=models.BooleanField(default=False, verbose_name='Do you consider yourself a tech-savvy person?'),
        ),
    ]
