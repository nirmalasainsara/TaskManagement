# Generated by Django 2.2 on 2021-05-12 07:52

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Projects',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300)),
                ('description', models.TextField()),
                ('duration', models.DateTimeField()),
                ('image', models.ImageField(upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('taskname', models.CharField(max_length=300)),
                ('taskdescription', models.TextField()),
                ('startdate', models.DateTimeField()),
                ('enddate', models.DateTimeField()),
                ('assign', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='task_assign', to=settings.AUTH_USER_MODEL)),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='task.Projects')),
                ('reporter', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='task_reporter', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
