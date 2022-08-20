# Generated by Django 4.1 on 2022-08-20 06:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("user", "0002_rename_noti_temp_profile_noti_tempo"),
    ]

    operations = [
        migrations.CreateModel(
            name="Room",
            fields=[
                ("RID", models.AutoField(primary_key=True, serialize=False)),
                ("start_time", models.DateField(auto_now_add=True)),
                ("end_time", models.DateField(auto_now_add=True)),
                (
                    "profile",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="profile",
                        to="user.profile",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Detail",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("focus", models.BooleanField(default=True)),
                ("duration", models.DurationField(blank=True)),
                ("start_focus", models.DateField(auto_now_add=True)),
                ("end_focus", models.DateField(auto_now_add=True)),
                (
                    "profile",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="detail",
                        to="user.profile",
                    ),
                ),
                (
                    "room",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="detail",
                        to="record.room",
                    ),
                ),
            ],
        ),
    ]