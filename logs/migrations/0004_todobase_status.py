# Generated by Django 4.0.5 on 2022-08-02 08:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('logs', '0003_delete_todobase2_todobase_ank1_todobase_ank2_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='todobase',
            name='status',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
    ]
