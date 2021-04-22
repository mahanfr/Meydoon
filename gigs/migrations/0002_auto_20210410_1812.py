# Generated by Django 3.1.7 on 2021-04-10 13:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gigs', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gig',
            name='experience',
            field=models.PositiveSmallIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='plan',
            name='price',
            field=models.PositiveIntegerField(default=5000),
        ),
        migrations.AlterField(
            model_name='userrate',
            name='rate',
            field=models.PositiveSmallIntegerField(default=1),
        ),
    ]