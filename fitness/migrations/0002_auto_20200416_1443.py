# Generated by Django 3.0.5 on 2020-04-16 14:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('fitness', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='fitnessclass',
            name='comment',
        ),
        migrations.AddField(
            model_name='fitnessclass',
            name='comment',
            field=models.ForeignKey(blank=True, default=1, on_delete=django.db.models.deletion.CASCADE, related_name='fitness', to='fitness.Comment'),
            preserve_default=False,
        ),
    ]