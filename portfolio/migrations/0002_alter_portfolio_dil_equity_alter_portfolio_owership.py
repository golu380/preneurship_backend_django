# Generated by Django 4.0.3 on 2022-05-09 14:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='portfolio',
            name='dil_equity',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='portfolio',
            name='owership',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
