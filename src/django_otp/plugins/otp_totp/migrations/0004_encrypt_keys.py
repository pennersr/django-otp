from django.db import migrations


def forwards(apps, schema_editor):
    TOTPDevice = apps.get_model("otp_totp", "TOTPDevice")
    for d in TOTPDevice.objects.all().iterator():
        d.encrypted_key = d.key
        d.save(update_fields=["encrypted_key"])


class Migration(migrations.Migration):

    dependencies = [
        ("otp_totp", "0003_totpdevice_encrypted_key"),
    ]

    operations = [
        migrations.RunPython(forwards),
    ]
