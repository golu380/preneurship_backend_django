# Generated by Django 4.0.3 on 2022-05-15 18:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0007_alter_portfolio_profile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='portfolio',
            name='profile',
            field=models.TextField(blank=True, null=True),
        ),
    ]
