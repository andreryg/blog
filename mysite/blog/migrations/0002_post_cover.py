# Generated by Django 2.2.6 on 2019-10-15 08:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='cover',
            field=models.ImageField(default='images/cogito_thumb.jpg', upload_to='css/media/images/'),
        ),
    ]
