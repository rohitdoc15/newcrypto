# Generated by Django 4.1.5 on 2023-01-05 12:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('firstapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='farzi',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('farzi_num', models.CharField(max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='coinname',
            name='rc',
            field=models.FloatField(default=0),
        ),
    ]