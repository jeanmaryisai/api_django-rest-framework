# Generated by Django 4.2 on 2023-04-18 14:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Stats',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('rutshelle', models.IntegerField()),
                ('darlinedesca', models.IntegerField()),
                ('vanessa_desireofficiel', models.IntegerField()),
                ('fatiful', models.IntegerField()),
                ('aniealerte', models.IntegerField()),
                ('tafaayiti', models.IntegerField()),
                ('bedjineofficiel', models.IntegerField()),
                ('blondedyferdinandshop', models.IntegerField()),
            ],
        ),
    ]
