# Generated by Django 2.2.1 on 2019-11-15 15:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0008_category_code_no'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='title',
            field=models.CharField(default='', max_length=200, null=True),
        ),
    ]
