# Generated by Django 2.0 on 2017-12-15 01:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='BimbinganProposal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hasil', models.TextField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Proposal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('judul', models.TextField(max_length=500)),
                ('katakunci', models.TextField(max_length=500)),
                ('ringkasan', models.TextField(max_length=1000)),
                ('npm', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='base.Mahasiswa')),
            ],
        ),
    ]
