# Generated by Django 4.1.2 on 2022-10-28 12:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0005_team_linkdin_alter_team_facebook_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='team',
            name='image',
            field=models.ImageField(default='default.png', upload_to='team/'),
        ),
    ]