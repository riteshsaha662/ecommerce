# Generated by Django 4.1.4 on 2023-02-01 09:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0002_alter_post_desc'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='desc',
            field=models.TextField(),
        ),
    ]
