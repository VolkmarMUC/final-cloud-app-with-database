# Generated by Django 3.1.3 on 2022-07-01 12:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('onlinecourse', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question_text', models.TextField(verbose_name='Question Text')),
                ('grade', models.IntegerField(verbose_name=0)),
                ('lesson', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='onlinecourse.lesson')),
            ],
        ),
    ]
