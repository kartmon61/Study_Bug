# Generated by Django 2.2.7 on 2019-11-14 14:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0002_auto_20191114_1416'),
    ]

    operations = [
        migrations.AlterField(
            model_name='license',
            name='licences',
            field=models.CharField(choices=[('a', '산업기사자격증'), ('b', '물류기사자격증')], default=True, max_length=2),
        ),
    ]
