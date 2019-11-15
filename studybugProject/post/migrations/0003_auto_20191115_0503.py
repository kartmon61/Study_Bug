# Generated by Django 2.2.7 on 2019-11-15 05:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0002_auto_20191115_0359'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=200, null=True)),
            ],
        ),
        migrations.RenameField(
            model_name='student',
            old_name='title',
            new_name='category',
        ),
        migrations.AlterField(
            model_name='student',
            name='body',
            field=models.TextField(max_length=200),
        ),
        migrations.AlterField(
            model_name='student',
            name='rate',
            field=models.CharField(max_length=200),
        ),
    ]
