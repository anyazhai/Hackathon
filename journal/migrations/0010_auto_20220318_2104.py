# Generated by Django 3.2.12 on 2022-03-18 15:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('journal', '0009_entry_starred'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='entry',
            options={'ordering': ('-date',)},
        ),
        migrations.AddIndex(
            model_name='entry',
            index=models.Index(fields=['title', 'starred'], name='journal_ent_title_0ecec1_idx'),
        ),
    ]