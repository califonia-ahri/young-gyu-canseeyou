# Generated by Django 4.1 on 2022-08-20 17:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("record", "0008_alter_detail_end_focus_alter_detail_start_focus_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="detail",
            name="end_focus",
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name="detail",
            name="start_focus",
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name="party",
            name="end_time",
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name="party",
            name="start_time",
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]