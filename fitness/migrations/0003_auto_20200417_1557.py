# Generated by Django 3.0.5 on 2020-04-17 15:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fitness', '0002_bookedclass_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='borough',
            name='fitnessclass',
            field=models.ManyToManyField(blank=True, related_name='fitness', to='fitness.FitnessClass'),
        ),
    ]
