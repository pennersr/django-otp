from django.db import migrations


def forwards(apps, schema_editor):
    StaticToken = apps.get_model("otp_static", "StaticToken")
    for st in StaticToken.objects.all().iterator():
        st.encrypted_token = st.token
        st.save(update_fields=["encrypted_token"])


class Migration(migrations.Migration):

    dependencies = [
        ("otp_static", "0003_statictoken_encrypted_token"),
    ]

    operations = [
        migrations.RunPython(forwards),
    ]
