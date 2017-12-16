# Generated by Django 2.0 on 2017-12-16 11:03

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0003_auto_20171216_0932'),
        ('proposal', '0003_auto_20171216_0932'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sidang',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tanggal', models.DateField(default=django.utils.timezone.now)),
                ('dospem', models.BooleanField(default=False)),
            ],
        ),
        migrations.RenameField(
            model_name='proposal',
            old_name='npm',
            new_name='akun',
        ),
        migrations.AddField(
            model_name='bimbinganproposal',
            name='proposal',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='proposal.Proposal'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='proposal',
            name='dospem',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.DO_NOTHING, to='base.Dosen'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='bimbinganproposal',
            name='tanggal',
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='sidang',
            name='proposal',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='proposal.Proposal'),
        ),
    ]
