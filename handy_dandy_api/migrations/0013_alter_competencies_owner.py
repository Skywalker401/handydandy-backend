# Generated by Django 4.1.2 on 2022-10-26 22:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('handy_dandy_api', '0012_competencies_owner'),
    ]

    operations = [
        migrations.AlterField(
            model_name='competencies',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='handy_dandy_api.user'),
        ),
    ]
