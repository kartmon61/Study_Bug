# Generated by Django 2.2.7 on 2019-11-14 14:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='license',
            name='name',
        ),
        migrations.AddField(
            model_name='license',
            name='licences',
            field=models.CharField(choices=[('a', '산업기사자격증'), ('b', '물류기사자격증')], default='null', max_length=2),
        ),
    ]
