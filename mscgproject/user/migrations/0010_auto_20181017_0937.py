# Generated by Django 2.1.2 on 2018-10-17 09:37

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import user.models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0009_auto_20181016_1647'),
    ]

    operations = [
        migrations.AlterField(
            model_name='leave',
            name='endday',
            field=models.DateField(default=django.utils.timezone.now, verbose_name='请假结束日期'),
        ),
        migrations.AlterField(
            model_name='leave',
            name='startday',
            field=models.DateField(default=django.utils.timezone.now, verbose_name='请假起始日期'),
        ),
        migrations.AlterField(
            model_name='notice',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='user.User', verbose_name='发送人ID'),
        ),
        migrations.AlterField(
            model_name='out',
            name='endday',
            field=models.DateField(default=django.utils.timezone.now, verbose_name='外出结束日期'),
        ),
        migrations.AlterField(
            model_name='out',
            name='startday',
            field=models.DateField(default=django.utils.timezone.now, verbose_name='外出起始日期'),
        ),
        migrations.AlterField(
            model_name='performance',
            name='salaryMonth',
            field=models.DateField(default=django.utils.timezone.now, verbose_name='日期'),
        ),
        migrations.AlterField(
            model_name='staff',
            name='birth',
            field=models.DateField(default=django.utils.timezone.now, verbose_name='生日'),
        ),
        migrations.AlterField(
            model_name='staff',
            name='hiredate',
            field=models.DateField(default=django.utils.timezone.now, verbose_name='入职日期'),
        ),
        migrations.AlterField(
            model_name='staff',
            name='photo',
            field=models.ImageField(default='test_1/1.png', upload_to=user.models.user_photo_path),
        ),
        migrations.AlterField(
            model_name='staff',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='user.User'),
        ),
    ]