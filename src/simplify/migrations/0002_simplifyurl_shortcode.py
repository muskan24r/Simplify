# Generated by Django 2.2.1 on 2019-05-13 14:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('simplify', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='simplifyurl',
            name='shortcode',
            field=models.CharField(blank=True, max_length=15, unique=True),
        ),
    ]
