# Generated by Django 2.1.2 on 2018-10-23 09:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0022_auto_20181023_0909'),
    ]

    operations = [
        migrations.RenameField(
            model_name='message',
            old_name='title',
            new_name='message_title',
        ),
        migrations.RenameField(
            model_name='notice',
            old_name='title',
            new_name='notice_title',
        ),
        migrations.AlterField(
            model_name='staff',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='user.User'),
        ),
    ]