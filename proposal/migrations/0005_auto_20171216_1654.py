# Generated by Django 2.0 on 2017-12-16 16:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('proposal', '0004_auto_20171216_1103'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bimbinganproposal',
            name='proposal',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='propID', to='proposal.Proposal'),
        ),
        migrations.AlterField(
            model_name='proposal',
            name='akun',
            field=models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, related_name='mhsAkun', to='base.Mahasiswa'),
        ),
        migrations.AlterField(
            model_name='sidang',
            name='proposal',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='propSid', to='proposal.Proposal'),
        ),
    ]