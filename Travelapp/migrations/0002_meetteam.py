# Generated by Django 4.1.3 on 2022-12-10 11:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Travelapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Meetteam',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('picture', models.ImageField(upload_to='pics')),
                ('team', models.CharField(max_length=250)),
                ('about', models.TextField()),
            ],
        ),
    ]