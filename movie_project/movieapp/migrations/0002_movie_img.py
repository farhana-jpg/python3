# Generated by Django 5.0 on 2023-12-29 05:55

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("movieapp", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="movie",
            name="img",
            field=models.ImageField(default=1234, upload_to="gallery"),
            preserve_default=False,
        ),
    ]
