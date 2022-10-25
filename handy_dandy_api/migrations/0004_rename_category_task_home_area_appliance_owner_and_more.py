# Generated by Django 4.1.2 on 2022-10-25 08:29

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("handy_dandy_api", "0003_user_sid"),
    ]

    operations = [
        migrations.RenameField(
            model_name="task",
            old_name="category",
            new_name="home_area",
        ),
        migrations.AddField(
            model_name="appliance",
            name="owner",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.CASCADE,
                to=settings.AUTH_USER_MODEL,
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="task",
            name="owner",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.CASCADE,
                to=settings.AUTH_USER_MODEL,
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="user",
            name="email",
            field=models.EmailField(default=1, max_length=254),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name="HomeArea",
        ),
    ]
