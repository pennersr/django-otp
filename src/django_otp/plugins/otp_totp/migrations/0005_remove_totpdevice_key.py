# Generated by Django 4.1.1 on 2022-11-22 15:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("otp_totp", "0004_encrypt_keys"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="totpdevice",
            name="key",
        ),
    ]