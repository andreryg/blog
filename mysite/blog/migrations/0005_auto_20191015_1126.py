# Generated by Django 2.2.6 on 2019-10-15 09:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20191015_1109'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='cover',
            field=models.ImageField(default='images/cogito_thumb.jpg', upload_to='images/'),
        ),
    ]
