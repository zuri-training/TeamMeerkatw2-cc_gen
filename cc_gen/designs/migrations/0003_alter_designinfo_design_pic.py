# Generated by Django 4.1.2 on 2022-12-14 01:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('designs', '0002_remove_designinfo_likes_designinfo_liked_likes'),
    ]

    operations = [
        migrations.AlterField(
            model_name='designinfo',
            name='design_pic',
            field=models.ImageField(default='default.png', upload_to='designs_pics'),
        ),
    ]
