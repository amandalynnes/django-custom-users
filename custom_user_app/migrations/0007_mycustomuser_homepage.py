# Generated by Django 3.1.7 on 2021-02-19 17:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('custom_user_app', '0006_auto_20210219_1626'),
    ]

    operations = [
        migrations.AddField(
            model_name='mycustomuser',
            name='homepage',
            field=models.URLField(blank=True, null=True),
        ),
    ]