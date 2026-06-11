from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("djangocms_form_builder", "0003_auto_20230129_1950"),
    ]

    operations = [
        migrations.CreateModel(
            name="HiddenField",
            fields=[],
            options={
                "verbose_name": "Hidden field",
                "proxy": True,
                "indexes": [],
                "constraints": [],
            },
            bases=("djangocms_form_builder.formfield",),
        ),
    ]
