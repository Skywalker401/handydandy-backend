# Generated by Django 4.1.2 on 2022-10-25 08:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        (
            "handy_dandy_api",
            "0004_rename_category_task_home_area_appliance_owner_and_more",
        ),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="email",
            field=models.EmailField(default="", max_length=254),
        ),
    ]