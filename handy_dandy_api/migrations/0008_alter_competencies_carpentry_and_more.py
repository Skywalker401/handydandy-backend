# Generated by Django 4.1.2 on 2022-10-26 19:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('handy_dandy_api', '0007_remove_competencies_owner_remove_task_appliance_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='competencies',
            name='carpentry',
            field=models.BooleanField(),
        ),
        migrations.AlterField(
            model_name='competencies',
            name='electrical',
            field=models.BooleanField(),
        ),
        migrations.AlterField(
            model_name='competencies',
            name='hvac',
            field=models.BooleanField(),
        ),
        migrations.AlterField(
            model_name='competencies',
            name='plumbing',
            field=models.BooleanField(),
        ),
    ]