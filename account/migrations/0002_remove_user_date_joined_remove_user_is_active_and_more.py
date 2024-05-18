# Generated by Django 5.0.3 on 2024-05-18 08:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("account", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="user",
            name="date_joined",
        ),
        migrations.RemoveField(
            model_name="user",
            name="is_active",
        ),
        migrations.RemoveField(
            model_name="user",
            name="is_staff",
        ),
        migrations.AlterField(
            model_name="user",
            name="is_superuser",
            field=models.BooleanField(
                default=False,
                help_text="Designates that this user has all permissions without explicitly assigning them.",
                verbose_name="superuser status",
            ),
        ),
        migrations.AlterField(
            model_name="user",
            name="last_login",
            field=models.DateTimeField(
                blank=True, null=True, verbose_name="last login"
            ),
        ),
    ]