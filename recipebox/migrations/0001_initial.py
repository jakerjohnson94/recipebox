# Generated by Django 2.1.7 on 2019-03-05 19:05

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
            name='Author',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bio', models.TextField(verbose_name='Brief bio about the author')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Recipe',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Title of recipe')),
                ('description', models.CharField(max_length=50, verbose_name='Description of the title')),
                ('time_required', models.IntegerField(verbose_name='Time Required to make recipe')),
                ('instructions', models.TextField(verbose_name='Recipe instructions')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='recipebox.Author')),
            ],
        ),
    ]