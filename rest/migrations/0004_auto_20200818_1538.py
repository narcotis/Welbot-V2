# Generated by Django 3.0.8 on 2020-08-18 06:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('rest', '0003_delete_school_lecture'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='kind',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.PROTECT, to='rest.Infrastructure'),
            preserve_default=False,
        ),
        migrations.CreateModel(
            name='Cul_facility',
            fields=[
                ('id', models.IntegerField()),
                ('name', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('kind', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='rest.Infrastructure')),
            ],
        ),
        migrations.AddField(
            model_name='culture_event',
            name='kind',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.PROTECT, to='rest.Cul_facility'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='exhibition',
            name='kind',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.PROTECT, to='rest.Cul_facility'),
            preserve_default=False,
        ),
    ]
