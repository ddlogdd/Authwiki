# Generated by Django 4.1 on 2022-08-13 06:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Authwiki', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comments',
            old_name='library',
            new_name='authwiki',
        ),
    ]
