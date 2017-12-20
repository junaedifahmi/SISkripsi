# Generated by Django 2.0 on 2017-12-16 09:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_auto_20171216_0825'),
    ]

    operations = [
        migrations.AddField(
            model_name='dosen',
            name='id',
            field=models.AutoField(auto_created=True, default=1, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='mahasiswa',
            name='id',
            field=models.AutoField(auto_created=True, default=1, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='dosen',
            name='akunDsn',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='base.User'),
        ),
        migrations.AlterField(
            model_name='mahasiswa',
            name='akunMhs',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='base.User'),
        ),
    ]